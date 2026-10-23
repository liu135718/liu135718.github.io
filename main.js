const videos = [...document.querySelectorAll('video')];
const resumeTimes = new WeakMap();
// The first project demo is the main entry point; let it buffer while the page is read.
if (videos[0]) videos[0].preload = 'auto';
const showPoster = video => {
  if (video.dataset.poster) {
    video.poster = video.dataset.poster;
    delete video.dataset.poster;
  }
};

const hasPlayingVideo = video => videos.some(other => other !== video && !other.paused && !other.ended);
const primeVideo = video => {
  showPoster(video);
  if (navigator.connection?.saveData || hasPlayingVideo(video)) return;
  // Only one nearby demo should buffer ahead; this keeps the first click responsive
  // on a slow connection without making all seven videos compete for bandwidth.
  videos.forEach(other => {
    if (other !== video && other.preload === 'auto') other.preload = 'metadata';
  });
  video.preload = 'auto';
};

// Read duration and seek information shortly before a demo enters the viewport.
// Keep distant videos at preload="none" so they do not compete for bandwidth.
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(entry => entry.isIntersecting);
    visible.forEach(({ target: video }) => showPoster(video));
    if (visible.length) {
      primeVideo(visible[0].target);
      visible.slice(1).forEach(({ target: video }) => {
        if (video.preload === 'none') video.preload = 'metadata';
      });
      visible.forEach(({ target: video }) => observer.unobserve(video));
    }
  }, { rootMargin: '200px 0px' });
  videos.forEach(video => observer.observe(video));
} else {
  videos.forEach(showPoster);
}

videos.forEach(video => {
  const prepare = () => {
    primeVideo(video);
  };
  video.addEventListener('pointerenter', prepare);
  video.addEventListener('focus', prepare);
  video.addEventListener('loadedmetadata', () => {
    const position = resumeTimes.get(video);
    if (position !== undefined) {
      resumeTimes.delete(video);
      video.currentTime = position;
    }
  });
  video.addEventListener('pointerdown', prepare);
  video.addEventListener('touchstart', prepare, { passive: true });
  video.addEventListener('play', () => {
    primeVideo(video);
    videos.forEach(other => {
      if (other === video) return;
      other.pause();
      other.preload = 'none';
      // Cancel speculative downloads while preserving the viewer's position.
      if (other.networkState !== HTMLMediaElement.NETWORK_EMPTY) {
        if (other.currentTime > 0 && !other.ended) resumeTimes.set(other, other.currentTime);
        other.load();
      }
    });
  });
});

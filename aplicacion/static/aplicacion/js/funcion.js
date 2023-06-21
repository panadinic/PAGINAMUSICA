
  const galleryContainer = document.querySelector('.gallery-container');
  const imageContainer = document.querySelector('.image-container');

  galleryContainer.addEventListener('scroll', () => {
    const scrollPos = galleryContainer.scrollLeft;
    imageContainer.style.transform = `translateX(-${scrollPos}px)`;
  });

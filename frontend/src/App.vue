<template>
  <div id="app">
    <UploadImage @imageUploaded="fetchImages" />
    <ImageList ref="imageList" />
  </div>
</template>

<script>
import UploadImage from './components/UploadImage.vue';
import ImageList from './components/ImageList.vue';

export default {
  components: {
    UploadImage,
    ImageList
  },
  methods: {
    fetchImages() {
      this.$refs.imageList.fetchImages();
    }
  },
  mounted() {
    this.fetchImages();
  }
};
</script>

<style>

</style>
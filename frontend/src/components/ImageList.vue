<template>
  <div class="project-container">
    <div class="card" v-for="image in images" :key="image.id">
      <img :src="image.image" alt="Image">
      <p>{{ "ID: " + image.id }}</p>
      <p>{{ "Description: " + image.description }}</p>
      <button class="delete-button" @click="deleteImage(image.id)">X</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      images: []
    };
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/projectimages/');
        this.images = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async deleteImage(id) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/projectimages/${id}/`);
        this.fetchImages();
      } catch (error) {
        console.error(error);
      }
    }
  },
  created() {
    this.fetchImages();
  }
};
</script>

<style scoped>

.project-container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.card {
  background-color: #181825;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 450px;
  position: relative;
  padding: 16px;
  text-align: center;
}

.card img {
  max-width: 100%;
  height: auto;
  margin-bottom: 12px;
}

.card p {
  margin: 8px 0;
  color: white;
}

.delete-button {
  background-color: #ff4d4d;
  border: none;
  color: white;
  padding: 8px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 14px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 4px;
  position: absolute;
  top: 16px;
  right: 16px;
}

button {
  border: 0;
  border-radius: 5px;
  outline: none;
  padding: 10px 15px;
  margin: 15px 0;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 500ms ease;
}

button:hover {
    transform: translateY(-5px);
}

projects-container {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-flow: wrap;
}

img {
  max-width: 450px;
  max-height: 250px;
  border-radius: 5px;
}

p {
  font: 57 12pt "Rubik Light";
}

</style>
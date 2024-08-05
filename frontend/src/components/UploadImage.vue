<template>
  <div class="container">
    <div class="textarea-row">
      <p>Send Image in DateBase:</p>
      <textarea v-model="description" placeholder="Enter image description"></textarea>
    </div>
    <div class="button-row">
      <label class="input-file">
        <input type="file" @change="onFileChange">
        <span>Choose image</span>
      </label>
    </div>
    <div v-if="selectedFileName" class="selected-file">
      <p class="selected_file_text">{{ selectedFileName }}</p>
      <button class="remove_button" @click="removeSelectedFile">X</button>
    </div>
    <div class="upload-row">
      <button class="upload_button" @click="uploadImage" :disabled="!image || !description">Upload</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      image: null,
      description: '',
      selectedFileName: null
    };
  },
  methods: {
    onFileChange(event) {
      this.image = event.target.files[0];
      this.selectedFileName = this.image ? this.image.name : null;
    },
    removeSelectedFile() {
      this.image = null;
      this.selectedFileName = null;
    },
    async uploadImage() {
      let formData = new FormData();
      formData.append('image', this.image);
      formData.append('description', this.description);

      try {
        await axios.post('http://127.0.0.1:8000/api/projectimages/', formData);
        this.$emit('imageUploaded');
        this.image = null;
        this.description = '';
        this.selectedFileName = null;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>

.container{
  display: flex;
  flex-direction: column;
  text-align: center;
}

.upload_button {
  border: 0;
  border-radius: 5px;
  outline: none;
  padding: 15px 35px;
  background-color: #7f2a54;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 500ms ease;
  margin: 20px 0;
}

.upload_button:hover {
  transform: translateY(-5px);
}

textarea {
  background-color: #181825;
  color: white;
  font: 57 10pt "Rubik Medium";
  width: 450px;
  min-height: 80px;
  max-height: 300px;
  resize: vertical;
  overflow: hidden;
  transition: height .2s linear;
  padding: 10px;
  margin: 30px 0 0 0;
  max-width: 100%;
  line-height: 1.5;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-shadow: 1px 1px 1px #999;
}

.input-file span {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  text-decoration: none;
  font-size: 14px;
  vertical-align: middle;
  color: rgb(255 255 255);
  text-align: center;
  border-radius: 4px;
  background-color: #419152;
  background-color: #324184;
  line-height: 22px;
  height: 40px;
  padding: 10px 20px;
  box-sizing: border-box;
  border: none;
  margin: 20px 0;
  transition: background-color 0.2s;
}

.input-file input[type=file] {
  position: absolute;
  z-index: -1;
  opacity: 0;
  display: block;
  width: 0;
  height: 0;
}

.input-file:hover span {
  background-color: #2fcde6;
}
.input-file:active span {
  background-color: #43b7ff;
}

.input-file input[type=file]:disabled + span {
  background-color: #eee;
}

.selected-file {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
}

.selected-file p {
  margin: 5px 0;
}

.selected_file_text {
  font: 57 14pt "Rubik Medium";
}

.remove_button{
  background: rgb(200,30,21);
  background: radial-gradient(circle, rgba(200,30,21,1) 0%, rgba(117,0,0,1) 100%);
  border: 0;
  border-radius: 5px;
  padding: 15px 15px;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 500ms ease;
  margin: 20px 0;
}
</style>
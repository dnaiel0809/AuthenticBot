@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>
    <div class="container">
      <div class="bg-light">
        <h2>Welcome to the Supportive Communication Training Session!</h2>

        <!-- <p><br /></p> -->
        <p style="font-size: 1.2rem">
          In this session, you'll gain foundational skills in supportive
          communication and have the chance to apply them practically. We'll
          cover the basics of conveying support and empathy, and then present
          real-life online support-seeking posts. Your task is to craft
          supportive and empathetic responses for each.
        </p>
      </div>
      <center>
        <el-button @click="nextpage" type="primary" style="margin: 16px"
          >Next</el-button
        >
      </center>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

import http from "@/http";
import VueMarkdown from "vue-markdown";
import EasyMDE from "easymde";
import "easymde/dist/easymde.min.css";
import VueSimpleRangeSlider from "vue-simple-range-slider/vue2";
import "vue-simple-range-slider/vue2/css";
import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

// Import Bootstrap and BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import ElementUI from 'element-ui';

Vue.use(ElementUI);

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);

export default {
  name: "TrainingSession",
  components: { EasyMDE },

  mounted() {
    this.fetchData();
    // this.cannotGoback();
    this.scrollToTop();
  },
  data() {
    return {
      text: "",
      currentTask: 0,
      Pid: "",
      loading: true,
      condition: "",
    };
  },

  methods: {
    scrollToTop() {
      window.scrollTo(1, 2);
    },
    cannotGoback() {
      window.onpopstate = function () {
        history.go(1);
      };
    },
    jumpyTo(url) {
      if (this.$router.currentRoute.path !== url) {
        this.$router.push({
          path: url,
          query: { Pid: this.Pid, condition: this.condition },
        });
      }
    },
    messagePop(type, message) {
      this.$message({
        message: `${message}`,
        type: `${type}`,
      });
    },
    fetchData() {
      console.log("Params: ", this.$route.query.currentTask);
      console.log("Params: ", this.$route.query.Pid);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
    },

    nextpage() {
      this.jumpyTo("/training_session_2");
    },
  },
};
</script>

<style scoped>
.container {
  background: white;
  width: 75%;
  height: auto;
  margin: auto;
}
.header {
  margin-left: 4em;
  /*margin-top: 4em;*/
  padding-top: 4em;
  display: flex;
}

.button {
  /*width: 100px;*/
  width: 10%;
}

.drop-item {
  /*width: 500px;*/
  font-family: ColfaxAI, helvetica, sans-serif;
  font-size: small;
  /*white-space: normal;*/
  /*word-wrap: break-word;*/
}

.translate-container {
  padding: 20px;
}

.grid-content {
  height: 550px;
  border-radius: 4px;
  margin-bottom: 20px;
  padding-left: 4em;
}

.grid-content-post {
  height: 350px;
  border-radius: 4px;
  margin-bottom: 20px;
  padding-left: 4em;
}

.grid-content-post2 {
  height: 500px;
  border-radius: 4px;
  margin-bottom: 20px;
  padding-left: 4em;
}

.slider-content {
  height: 450px;
  border-radius: 4px;
  margin-bottom: 20px;
  padding-left: 4em;
  padding-right: 4em;
}

.bg-light {
  padding: 20px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.textarea {
  padding-top: 1em;
  padding-left: 1em;
  padding-right: 1em;
  padding-bottom: 1em;
  height: 550px;

  /*font-family: 'Arial', sans-serif; !* 这将更改字体 *!*/
  font-family: "Roboto", sans-serif;
  font-size: 16px; /* 这将更改字体大小 */
  color: #333; /* 这将更改文本颜色 */
  line-height: 1.5; /* 这将更改行高 */
  letter-spacing: 0.05em; /* 这将更改字符间距 */
  text-align: justify; /* 这将使文本两端对齐 */
  overflow-y: scroll;
}

.el-icon-arrow-down {
  font-size: 12px;
}

.el-menu-item i {
  float: right;
  margin-top: 5px;
  cursor: pointer;
}

.example {
  background: #ffffff;
  margin: 20px;
  border-color: #e7e7e7;
  padding: 40px;
}
.header-slot {
  background: #d4e6ff;
  padding: 20px 100px;
  position: sticky;
  top: 0;
  /* z-index: 10000; */
}
</style>

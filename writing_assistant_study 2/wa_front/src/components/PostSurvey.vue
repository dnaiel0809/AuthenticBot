@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div class="container">
    <iframe ref="Iframe" width="100%" height="1300px"></iframe>
    <!-- <b-row align-self="center"
      ><center>
        <el-button @click="submitWriting" type="primary">Next page</el-button>
      </center></b-row
    > -->
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

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);

export default {
  name: "PostSurvey",
  components: {
    // VueMarkdown,
    // EasyMDE,
    // VueSimpleRangeSlider,
  },

  mounted() {
    this.fetchData();
    this.uploadTime();
    this.scrollToTop();
    // this.enableEditMode();
    this.addSurveyListener();
    // this.enableOutputEditMode();

    //  检查是否是登录用户
  },
  data() {
    return {
      Pid: "",
      condition: "",
    };
  },

  methods: {
    fetchData() {
      console.log("Params: ", this.$route.query.currentTask);
      console.log("Params: ", this.$route.query.Pid);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
      this.addHashToLocation();
    },
    scrollToTop() {
      window.scrollTo(0, 2);
    },
    jumpyTo(url) {
      if (this.$router.currentRoute.path !== url) {
        this.$router.push(url);
      }
    },

    messagePop(type, message) {
      this.$message({
        message: `${message}`,
        type: `${type}`,
      });
    },

    
    addHashToLocation() {
      let params = "?PID=" + this.Pid + "&condition=" + this.condition;

      const iframe = this.$refs.Iframe;
      iframe.src =
        "https://nus.syd1.qualtrics.com/jfe/form/SV_3z1AEtLFLZ76pgy" + params;
    },

    submitWriting() {
      this.jumpyTo("/post_survey");
    },
    uploadTime() {
      http
        .post("/update_time_row/", {
          pid: this.Pid,
          training_start_1: sessionStorage.getItem("training_start_1"),
          training_start_2: sessionStorage.getItem("training_start_2"),
          training_start_3: sessionStorage.getItem("training_start_3"),
          training_end_1: sessionStorage.getItem("training_end_1"),
          training_end_2: sessionStorage.getItem("training_end_2"),
          training_end_3: sessionStorage.getItem("training_end_3"),
          main_task_start_1: sessionStorage.getItem("main_task_start_1"),
          main_task_start_2: sessionStorage.getItem("main_task_start_2"),
          main_task_start_3: sessionStorage.getItem("main_task_start_3"),
          main_task_end_1: sessionStorage.getItem("main_task_end_1"),
          main_task_end_2: sessionStorage.getItem("main_task_end_2"),
          main_task_end_3: sessionStorage.getItem("main_task_end_3"),
          editing_start_1: sessionStorage.getItem("editing_start_1"),
          editing_start_2: sessionStorage.getItem("editing_start_2"),
          editing_start_3: sessionStorage.getItem("editing_start_3"),
          editing_end_1: sessionStorage.getItem("editing_end_1"),
          editing_end_2: sessionStorage.getItem("editing_end_2"),
          editing_end_3: sessionStorage.getItem("editing_end_3"),
          question_start_1: sessionStorage.getItem("question_start_1"),
          question_start_2: sessionStorage.getItem("question_start_2"),
          question_start_3: sessionStorage.getItem("question_start_3"),
          question_end_1: sessionStorage.getItem("question_end_1"),
          question_end_2: sessionStorage.getItem("question_end_2"),
          question_end_3: sessionStorage.getItem("question_end_3"),
        })
        .then((res) => {
          console.log("success upload time");
        })
        .catch((e) => {
          console.log(e);
        });
      return;
    },
    addSurveyListener() {
      window.addEventListener("message", (e) => {
        console.log(e);
        if (
          e.origin.includes("https://nus.syd1.qualtrics.com") &&
          e.data.includes("QualtricsEOS|SV_3z1AEtLFLZ76pgy")
        ) {
          
          // window.location.href = "https://app.prolific.co/submissions/complete?cc=C7R2DB6M";
          window.location.href = "https://app.prolific.co/submissions/complete?cc=CIOBAECS";
        }
      });
    },
  },
};
</script>

<style scoped>
.container {
  background: white;
  width: 90%;
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
</style>

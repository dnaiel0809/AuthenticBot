@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>
    <div class="container">
      <p><br /></p>
      <p style="font-size: 1.2rem">
        You can now revise the message as needed. Feel free to make any changes
        if you see fit. Once you're happy with your response, kindly fill out
        the survey. The message will be saved and uploaded automatically. Note
        that this support message will be shared anonymously in an online peer
        support community.
      </p>
      <!-- <p>After you submit, you'll be asked to evaluate your written message.</p> -->

      <el-row :gutter="20">
        <el-col :span="12">
          <div v-loading="loading" element-loading-text="loading...">
            <!--Task1-->
            <div v-show="post == '1'" class="grid-content-post2 bg-light">
              <!-- <div class="grid-content-post2 bg-light"> -->
              <div
                class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                data-animation-name=""
                data-animation-duration="0"
                data-animation-direction=""
              >
                <h5 style="text-align: left">
                  <span style="font-size: 1.8rem">
                    Subject: My fiance M/30 said something shocking to me 27/F

                    <br />
                  </span>
                </h5>

                <hr />

                <p><br /></p>
                <p id="isPasted" style="font-size: 1.2rem">
                  My fiance M/30 and I 27/F have been together for a year and so
                  we took an anniversary vacation. While we were traveling back,
                  I told him that I wanted to dye my hair, and he said "You
                  really think your hair is the issue?" When I asked what he
                  meant, he said "Look at the way your shirt is stretched over
                  your gut" When I reminded him I've lost 20 pounds and he's
                  always complimented my body, he said "That was laying down.
                  Standing up I see your shirt stretched over your gut and it
                  looks so disgusting to me" I started crying from shock and he
                  said "I'm not dealing with you crying over every little thing,
                  this is pathetic, I'm telling you the truth so you don't get
                  fat." (I work out 5x a week, cook us healthy meals, and avoid
                  sweets.) We are set to move and get married in 2 months. I
                  love him and the life we've built but I am devastated by his
                  comments. I need advice on what to do next, and if he's right
                  and I'm being too sensitive. TIA!
                </p>
                <p><br /><br /><br /></p>
              </div>
              <!-- </div> -->
            </div>

            <!--Task2-->
            <!-- <div
              
              class="grid-content-post bg-light"
            > -->
            <div v-show="post == '2'" class="grid-content-post2 bg-light">
              <div
                class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                data-animation-name=""
                data-animation-duration="0"
                data-animation-direction=""
              >
                <h5 style="text-align: left">
                  <span style="font-size: 1.8rem">
                    Subject: Just found out I'm being let go from my job today.
                    What the fuck do i do?

                    <br />
                  </span>
                </h5>

                <hr />

                <p><br /></p>
                <p id="isPasted" style="font-size: 1.2rem">
                  Been with the place for 3 years and for the first 2ish years,
                  i thought I found my forever place. We had a meeting today and
                  at the end of it, they mention that despite a lot of other
                  measures, they're going to have to make a small number of
                  staff cuts, and it turns out that after asking my boss, I was
                  one of the people they were letting go. It's really
                  frustrating. I was great at my job. The first year I had a 10%
                  raise and the second year I dealt with a lot of the extra work
                  that I did to finance and beyond my job description. But they
                  gave me a standard raise because of financials and now I'm
                  being let go. I'm absolutely devastated. I don't even know
                  where to begin besides updating my resume. I'm so gutted.
                </p>
                <p><br /><br /><br /></p>
              </div>
            </div>
            <!-- </div> -->
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-light" v-loading="loading">
            <div class="label_container" style="display: flex">
              <label
                style="
                  font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                  font-size: large;
                "
              ></label>
            </div>
            <textarea
              id="outputArea"
              ref="enableEditMode"
              class="textarea"
            ></textarea>
          </div>
        </el-col>
      </el-row>
      <!-- <div
        class="grid-content bg-light"
        v-loading="loading"
        element-loading-text="loading..."
      >
        <div class="label_container" style="display: flex">
          <label
            style="
              font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
              font-size: large;
            "
          ></label>
        </div>
        <textarea
          id="outputArea"
          ref="enableEditMode"
          class="textarea"
        ></textarea>
        
      </div> -->
      <div>
        <iframe ref="Iframe" width="100%" height="1300px"></iframe>
        <center>
          <el-button
            @click="nextpage"
            type="primary"
            style="margin: 10px"
            v-show="nextPageBool"
            >next page</el-button
          >
        </center>
      </div>
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
import ElementUI from "element-ui";

Vue.use(ElementUI);
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);

export default {
  name: "EditWriting_2",
  components: { EasyMDE },

  mounted() {
    this.fetchData();
    this.enableEditMode();
    this.addSurveyListener();
    // this.cannotGoback();
    this.scrollToTop();
  },
  data() {
    return {
      text: "",
      Pid: "",
      loading: true,
      nextPageBool: false,
      condition: "",
      post: "",
    };
  },

  methods: {
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
    scrollToTop() {
      window.scrollTo(1, 2);
    },
    messagePop(type, message) {
      this.$message({
        message: `${message}`,
        type: `${type}`,
      });
    },
    fetchData() {
      console.log("Params: ", this.$route.query.Pid);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
      this.post = sessionStorage.getItem("main_2");
      this.addHashToLocation();
      console.log(this.post);
      sessionStorage.setItem("editing_start_" + this.post, Date.now());
      http
        .post("/get_google_sheet_mimic_task/", {
          pid: this.Pid,
          post: this.post,
        })
        .then((res) => {
          this.loading = false;
          this.markdownEditor.value(res.data.mimic_output);
          console.log("mimic_output", res.data.mimic_output);
        })
        .catch((e) => {
          console.log(e);
        });
    },
    enableEditMode() {
      this.editMode = true;
      const vm = this;
      this.$nextTick(() => {
        if (!this.markdownEditor) {
          this.markdownEditor = new EasyMDE({
            element: this.$refs.markdownEditor,
          });

          //设计样式
          // const codemirrorScroll = document.getElementsByClassName('CodeMirror-scroll')[0];
          const codemirrorScroll =
            document.getElementsByClassName("CodeMirror-scroll")[0];
          console.log("scoll");
          console.log(codemirrorScroll);
          if (codemirrorScroll) {
            codemirrorScroll.style.maxHeight = "400px";
            codemirrorScroll.style.overflowY = "auto";
            console.log("successfully set");
          }
          this.markdownEditor.value(this.text);
          this.markdownEditor.codemirror.on("change", () => {
            vm.text = vm.markdownEditor.value();
            console.log(vm.text); // 输出当前的输入值
          });
        }
      });
    },
    submitWriting() {
      sessionStorage.setItem("editing_end_" + this.post, Date.now());
      http
        .post("/upload_google_sheet_edited_task/", {
          pid: this.Pid,
          post: this.post,
          editedText: this.text,
        })
        .then((res) => {
          console.log("success", res.data.success);
          this.messagePop("success", "Successfully submit!");
          // this.jumpyTo("/writing_assitant_show");
        })
        .catch((e) => {
          console.log(e);
        });
    },
    nextpage() {
      this.submitWriting();

      this.jumpyTo("/post_survey");
    },
    addSurveyListener() {
      window.addEventListener("message", (e) => {
        console.log(e);
        if (
          e.origin.includes("https://nus.syd1.qualtrics.com") &&
          e.data.includes("QualtricsEOS|SV_6hzftT2MX5eWOua")
        ) {
          this.nextPageBool = true;
          console.log("survey end");
          this.nextpage();
        }
      });
    },
    addHashToLocation() {
      let params =
        "?PID=" +
        this.Pid +
        "&condition=" +
        this.condition +
        "&post=" +
        this.post;
      // history.pushState({}, null, this.$route.path + "#" + params);
      const iframe = this.$refs.Iframe;
      iframe.src =
        "https://nus.syd1.qualtrics.com/jfe/form/SV_6hzftT2MX5eWOua" + params;
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
  height: auto;
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
  height: auto;
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

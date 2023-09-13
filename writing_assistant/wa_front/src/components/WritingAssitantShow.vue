@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>

    <div class="container">
      <div v-show="condition != 3">
        <p style="font-size: 1.2rem">
          Great job on completing the training session!
        </p>
        <p style="font-size: 1.2rem">
          Now, let's move on to the main tasks. You'll be shown two
          support-seeking posts, presented one after the other. For each post,
          you'll also see an AI-generated response. Your task is to carefully
          review and evaluate this AI response.
        </p>
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 3">
        <p style="font-size: 1.2rem">
          Great job on completing the training session!
        </p>
        <p style="font-size: 1.2rem">
          Now, let's move on to the main tasks. You'll be shown two
          support-seeking posts, presented one after the other. For each post,
          craft a response using the skills you just learned. Once you're happy
          with your response, kindly fill out the survey. The message will be
          saved and uploaded automatically.
        </p>
      </div>
      <!-- <b-row v-show="currentTask != '2 ' && condition != 3" align="center">
        <p style="font-size: 2.5rem">Example of your support message:</p>
      </b-row> -->
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
          <div
            class="grid-content bg-light"
            v-loading="gLoading"
            element-loading-text="AI takes 30 to 60 seconds to generate content. Do not refresh the page."
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
              ref="markdownEditor"
              class="textarea"
            ></textarea>
          </div>
        </el-col>
      </el-row>
      <div v-loading="loading" element-loading-text="loading..." class="survey">
        <iframe
          v-show="surveyShow"
          ref="Iframe"
          width="100%"
          height="1300px"
        ></iframe>
        <b-col align-v="center">
          <!-- <b-row align-self="center"
            ><center>
              <p>Please first submit the survey then go to the next page.</p>
            </center></b-row
          > -->

          <b-row align-self="center"
            ><center>
              <el-button
                @click="submitWriting"
                type="primary"
                v-show="nextPageBool"
                style="margin: 10px"
                >Next page</el-button
              >
            </center></b-row
          >
        </b-col>
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
  name: "WritingAssitantShow",
  components: {
    VueMarkdown,
    EasyMDE,
    VueSimpleRangeSlider,
  },

  mounted() {
    this.fetchData();
    // this.enableEditMode();
      this.getExample();
    this.addSurveyListener();
    this.scrollToTop();
    //  检查是否是登录用户
  },
  data() {
    return {
      Pid: "",
      testData: "",
      edit: false,
      p_edit: false,
      sliderBool: false,
      markdownContent: "",
      prompts: null,
      my_prompts: null,
      drawer: false,
      my_drawer: false,
      direction: "rtl",

      Prompt:
        "Now you will write a supportive message (1-200 words) in response to the following support-seeking post.\
      A good supportive message might include 1. Emotional reactions: Express emotions such as warmth, compassion, and concern. \
      2. Interpretations: Convey understanding of feelings or experiences. 3. Explorations: Delve deeper into feelings and experiences, even if not directly mentioned.",

      promptV3_1:
        "Now you will write a supportive message (1-200 words) based on the linguistic style of a person.\
      I will first provide you with a few messages that the person wrote, and you need to learn the linguistic style,\
      including function words, formality, positivity, verbosity, and directness. No need to show the results of the linguistic style analysis.\n\
      Formality refers to the extent to which the text is formal. Positivity refers to the extent to which the text carries positive sentiments. \
      Verbosity pertains to the wordiness of the text. Directness refers to the extent to which the text explicitly reveals the writer’s intentions.",
      promptV3_2:
        "Then, write a supportive message in response to the following support-seeking post, based on the linguistic style you learned.\
      A good supportive message might include 1. Emotional reactions: Express emotions such as warmth, compassion, and concern. \
      2. Interpretations: Convey understanding of feelings or experiences. 3. Explorations: Delve deeper into feelings and experiences, even if not directly mentioned.",

      seekingPost: [
        "My fiance M/30 said something shocking to me 27/F. \n\
         My fiance M/30 and I 27/F have been together for a year and \
         so we took an anniversary vacation. While we were traveling back,\
         I told him that I wanted to dye my hair, and he said \"You really \
         think your hair is the issue?\" When I asked what he meant, he said\
        \"Look at the way your shirt is stretched over your gut\" When I \
        reminded him I've lost 20 pounds and he's always complimented my \
        body, he said \"That was laying down. Standing up I see your shirt \
        stretched over your gut and it looks so disgusting to me\" I started\
        crying from shock and he said \"I'm not dealing with you crying over\
        every little thing, this is pathetic, I'm telling you the truth so\
        you don't get fat.\" (I work out 5x a week, cook us healthy meals,\
        and avoid sweets.) We are set to move and get married in 2 months.\
        I love him and the life we've built but I am devastated by his\
        comments. I need advice on what to do next, and if he's right and\
        I'm being too sensitive. TIA!",

        "Just found out I'm being let go from my job today. What the fuck do i do?:\n\
        Been with the place for 3 years and for the first 2ish years,\
        i thought I found my forever place. We had a meeting today and\
        at the end of it, they mention that despite a lot of other measures,\
        they're going to have to make a small number of staff cuts, and it\
        turns out that after asking my boss, I was one of the people they were\
        letting go. It's really frustrating. I was great at my job. The first year\
        I had a 10% raise and the second year I dealt with a lot of the extra work\
        that I did to finance and beyond my job description. But they gave me a standard\
        raise because of financials and now I'm being let go. I'm absolutely devastated. \
        I don't even know where to begin besides updating my resume. I'm so gutted.",
      ],

      beforeEdit: "",
      inputText: "",

      mimicWriting: "",
      example1: sessionStorage.getItem("example1"),
      example2: sessionStorage.getItem("example2"),
      example3: sessionStorage.getItem("example3"),
      example4: sessionStorage.getItem("example4"),
      // models:['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4'],
      models: ["gpt-3.5-turbo", "gpt-3.5-turbo-16k"],
      selectedItem: "gpt-4",

      editMode: true,
      m_style: "",
      markdownEditor: null,

      markdownOutputEditor: null,

      toAttitudinalBool: false,
      toExperientialBool: false,
      toStyleLearningBool: true,
      loading: true,
      gLoading: true,
      surveyShow: false,
      text: "",
      nextPageBool: false,
      condition: -1,
      post: sessionStorage.getItem("main_1"),
    };
  },

  methods: {
    fetchData() {
      console.log("ID: ", this.$route.query);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
      
      
      // this.post = ;
      // this.example1 =
      // this.example2 =;
      // this.example3 = ;
      // this.example4 = ;
      console.log("post", this.post);
      console.log("post", this.example1);
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

    enableOutputEditMode() {
      const vm = this;
      this.$nextTick(() => {
        if (!this.markdownEditor) {
          this.markdownEditor = new EasyMDE({
            element: this.$refs.markdownEditor,
          });
          //设计样式
          const codemirrorScroll =
            document.getElementsByClassName("CodeMirror-scroll")[0];
          if (codemirrorScroll) {
            codemirrorScroll.style.maxHeight = "1000px";
            codemirrorScroll.style.overflowY = "auto";
            console.log("output successfully set");
          }

          if (this.condition == "3") {
            // this.markdownEditor.value(this.text);
            console.log("here");
            this.markdownEditor.codemirror.on("change", () => {
              vm.text = vm.markdownEditor.value();
              console.log(vm.text); // 输出当前的输入值
            });
          } else {
            this.markdownEditor.codemirror.setOption("readOnly", true);
          }
        }
      });
    },

    getExample() {
      this.gloading = true;

      this.loading = false;

      if (this.condition != "3") {
        console.log("getWrtingAssistantHelp");
        this.getWrtingAssistantHelp();
      } else {
        this.surveyShow = true;
      }
      sessionStorage.setItem("main_task_start_" + this.post, Date.now());
      this.enableOutputEditMode();

      this.addHashToLocation();
    },

    getWrtingAssistantHelp() {
      console.log("currentPost:", this.post);
      prompt = "";
      if (this.condition == "1") {
        prompt = `${this.promptV3_1}\n
                    [Writing style sample 1]\n
                     ${this.example1}\n
                     [Writing style sample 2]\n
                     ${this.example2}\n
                     [Writing style sample 3]\n
                     ${this.example3}\n
                     [Writing style sample 4]\n
                     ${this.example4}\n
                     ${this.promptV3_2}\n
                     [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n `;
      }
      if (this.condition == "2") {
        prompt = `${this.Prompt}\n
                     [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n `;
      }

      console.log("提交的数据是：", prompt);
      http
        .post("/writing_assistant/", {
          prompt: prompt,
          model: this.selectedItem,
          user: this.Pid,
          post: this.post,
        })
        .then((res) => {
          this.markdownEditor.value(res.data.content);
          this.mimicWriting = res.data.content;
          this.gLoading = false;
          this.surveyShow = true;
          console.log("output Text:", res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    submitWriting() {
      sessionStorage.setItem("main_task_end_" + this.post, Date.now());

      if (this.condition == "3") {
        http
          .post("/update_support_message/", {
            pid: this.Pid,
            post: this.post,
            text: this.text,
          })
          .then((res) => {
            console.log("success upload task");
            this.$router.push({
              path: "/writing_assitant_show_2",
              query: {
                Pid: this.Pid,
                condition: this.condition,
              },
            });
          })
          .catch((e) => {
            console.log(e);
          });
      }
      this.$router.push({
        path: "/edit_writing",
        query: {
          Pid: this.Pid,
          condition: this.condition,
        },
      });
    },

    addSurveyListener() {
      window.addEventListener("message", (e) => {
        console.log(e);
        if (
          e.origin.includes("https://nus.syd1.qualtrics.com") &&
          e.data.includes("QualtricsEOS|SV_1RmdtNoQdRouHie")
        ) {
          this.nextPageBool = true;
          console.log("survey end");
          this.submitWriting();
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
        "https://nus.syd1.qualtrics.com/jfe/form/SV_1RmdtNoQdRouHie" + params;
    },
  },
  updated() {
    if (this.condition == "3") this.gLoading = false;
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
.grid-content-2 {
  height: 450px;
  border-radius: 4px;
  margin-bottom: 20px;
  padding-left: 4em;
}

.grid-content-post {
  height: 450px;
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


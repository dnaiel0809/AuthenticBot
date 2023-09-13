@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>

    <div class="container">
      <div v-show="condition == 1">
        <p style="font-size: 1.2rem">This is the second post.</p>
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 2">
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 3">
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 4">
        <p style="font-size: 1.2rem">This is the second post.</p>
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 5">
        <p style="font-size: 1.2rem">This is the second post.</p>
        <p style="font-size: 1.2rem">
          At this stage, please <b>refrain from editing the response</b>. You'll
          have the opportunity to do so in the subsequent step.
        </p>
      </div>
      <div v-show="condition == 6">
        <p style="font-size: 1.2rem">
          Here is the AI-suggested message. Please carefully review and evaluate
          the message.
        </p>
        <p style="font-size: 1.2rem">
          At this stage, please refrain from editing the response. You'll have
          the opportunity to do so in the subsequent step.
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
                    Subject: I feel like I have nothing to do on the weekends
                    with my kids.

                    <br />
                  </span>
                </h5>

                <hr />

                <p><br /></p>
                <p style="font-size: 1.2rem">
                  I feel like a loser because my kids are getting older (7 and
                  8) and I never do anything on the weekends with them. They
                  just sit downstairs playing video games and watching tv. My
                  son has autism and doing anything with him is very difficult.
                  I myself do not have any parent friends that I can take my
                  kids on play dates with. My kids also don't really have many
                  friends either. I feel like I am socially isolated and my only
                  relief from home is work. I work overtime just to get out of
                  the house and not be home.
                </p>
                <p style="font-size: 1.2rem">
                  Can anyone here relate and how did you get past this phase of
                  your life? It's been like this for two years and I'm getting
                  more and more socially awkward with people in general due to
                  this social anxiety of feeling like myself and my kids just
                  don't have a life.
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
                    Subject: I’ve been staying up until 5am playing video games
                    and then sleeping until 3-4pm everyday

                    <br />
                  </span>
                </h5>

                <hr />

                <p><br /></p>
                <p style="font-size: 1.2rem">
                  I have no desire to get up earlier and do something with my
                  day even though if I could force myself I’d probably feel
                  better. It starts to get dark within an hour of waking up
                  usually and it’s so depressing but it keeps me isolated in my
                  “comfort zone”. Being up in the middle of the night feels
                  freeing for some reason, no one awake, no guilt for
                  responsibilities, I can sleep away the day and not feel guilty
                  about it.
                </p>
                <p style="font-size: 1.2rem">
                  But I’m wasting time and I want more than anything to feel
                  okay again. I want to start to get my life back to something
                  that I can derive some genuine enjoyment out of and move
                  forward with productive things.
                </p>
                <p style="font-size: 1.2rem">
                  I became depressed again about 10 months ago since my mom
                  passed and these past 10 months have gone by so fast, I’m
                  almost 26 and I’m scared at how fast time is moving without
                  any stability forming in my life.
                </p>
                <p><br /><br /><br /></p>
              </div>
            </div>
            <!-- </div> -->
            <!--Task3-->
            <!-- <div
              
              class="grid-content-post bg-light"
            > -->
            <div v-show="post == '3'" class="grid-content-post2 bg-light">
              <div
                class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                data-animation-name=""
                data-animation-duration="0"
                data-animation-direction=""
              >
                <h5 style="text-align: left">
                  <span style="font-size: 1.8rem">
                    Subject: My parents cannot afford to retire and do not own
                    their home.

                    <br />
                  </span>
                </h5>

                <hr />

                <p><br /></p>
                <p style="font-size: 1.2rem">
                  I (F22) am an only child to my parents (Mom is 62 and Dad is
                  60) who got started late in life. We lived in a trailer until
                  I was about 7 years old, and then we started renting our very
                  first home. Fast forward to now, they bought a home 4 years
                  ago after downsizing drastically but they still won't ever be
                  able to afford it. (We live in the Seattle area if that helps
                  paint a picture). They both work very laborious jobs and their
                  health is getting quite bad.
                </p>
                <p style="font-size: 1.2rem">
                  My mom was in the hospital and had 2 emergency operations last
                  month. Since then, they've been admitting to me how truly
                  depressed and scared they are. Not just for themselves, but
                  for me. I am dealing with my own health issues and lost my
                  career due to being unable to work. I don't have any money now
                  either and rely heavily on my parents as they are my only
                  family and support system. My dad told me that he's deeply
                  sorry he wasn't able to send me to college and that I will
                  have to find someone who is willing and financially able to
                  care for me soon, because my parents won't be around much
                  longer.
                </p>
                <p style="font-size: 1.2rem">
                  I am so scared of the future, and I feel like I'm the only 22
                  year old feeling the pressures of taking care of her aging
                  parents while having no money and poor health myself. I don't
                  know what to do. I wish my parents could stay home and take it
                  easy as they deserve... Any advice helps.
                </p>
                <p><br /><br /><br /></p>
              </div>
            </div>
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
          <el-button
            @click="humanWritingsubmitWriting"
            type="primary"
            v-show="nextPageBool"
            style="margin: 10px"
            >Submit</el-button
          >
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

          <b-row align-self="center"><center></center></b-row>
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
  name: "WritingAssitantShow_2",
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
      experience: "",
      feelings: "",
      // language style
      promptC1:
        "Now you will write a supportive message (1-200 words) based on the linguistic style of a person.\
      I will first provide you with a few messages that the person wrote, and you need to learn the linguistic style, including function words, formality, positivity, verbosity, and directness.\
      No need to show the results of the linguistic style analysis.\
      Formality refers to the extent to which the text is formal. Positivity refers to the extent to which the text carries positive sentiments. \
      Verbosity pertains to the wordiness of the text. Directness refers to the extent to which the text explicitly reveals the writer’s intentions.",

      promptC2:
        "Please write a supportive message in (1-200 words) response to the following support-seeking post. A good supportive message might: (1) express emotions such as warmth, compassion, and concern; (2) convey understanding and explanation of feelings or experiences; and (3) delve deeper into feelings and experiences, even if not directly mentioned.\
      Please also incorporate the person’s experiences into the supportive message. Please also incorporate the person’s experiences into the supportive message. ",

      promptC3:
        "Please write a supportive message in (1-200 words) response to the following support-seeking post. A good supportive message might: (1) express emotions such as warmth, compassion, and concern; (2) convey understanding and explanation of feelings or experiences; and (3) delve deeper into feelings and experiences, even if not directly mentioned.\
      Please also incorporate the person’s thoughts and feelings into the supportive message.",

      Prompt:
        "Now you will write a supportive message (1-200 words) in response to the following support-seeking post.\
      (1) express emotions such as warmth, compassion, and concern; (2) convey understanding and explanation of feelings or experiences;\
      and (3) delve deeper into feelings and experiences, even if not directly mentioned.",

      seekingPost: [
        "I feel like a loser because my kids are getting older (7 and 8) and I never do anything on the weekends with them.\
        They just sit downstairs playing video games and watching tv. My son has autism and doing anything with him is very difficult.\
        I myself do not have any parent friends that I can take my kids on play dates with. My kids also don't really have many friends either.\
        I feel like I am socially isolated and my only relief from home is work. I work overtime just to get out of the house and not be home.\
        Can anyone here relate and how did you get past this phase of your life?\
        It's been like this for two years and I'm getting more and more socially awkward with people in general due to this social anxiety of feeling like myself and my kids just don't have a life.",

        "I’ve been staying up until 5am playing video games and then sleeping until 3-4pm everyday \n\
        I have no desire to get up earlier and do something with my day even though if I could force myself I’d probably feel better.\
        It starts to get dark within an hour of waking up usually and it’s so depressing but it keeps me isolated in my “comfort zone”.\
        Being up in the middle of the night feels freeing for some reason, no one awake, no guilt for responsibilities, I can sleep away the day and not feel guilty about it.\
        But I’m wasting time and I want more than anything to feel okay again.\
        I want to start to get my life back to something that I can derive some genuine enjoyment out of and move forward with productive things.\
        I became depressed again about 10 months ago since my mom passed and these past 10 months have gone by so fast, I’m almost 26 and I’m scared at how fast time is moving without any stability forming in my life.",

        "My parents cannot afford to retire and do not own their home.\n\
        I (F22) am an only child to my parents (Mom is 62 and Dad is 60) who got started late in life. We lived in a trailer until I was about 7 years old,\
        and then we started renting our very first home. Fast forward to now, they bought a home 4 years ago after downsizing drastically but they still won't ever be able to afford it.\
        (We live in the Seattle area if that helps paint a picture). They both work very laborious jobs and their health is getting quite bad.\
        My mom was in the hospital and had 2 emergency operations last month. Since then, they've been admitting to me how truly depressed and scared they are.\
        Not just for themselves, but for me. I am dealing with my own health issues and lost my career due to being unable to work. I don't have any money now either and rely heavily on my parents as they are my only family and support system.\
        My dad told me that he's deeply sorry he wasn't able to send me to college and that I will have to find someone who is willing and financially able to care for me soon, because my parents won't be around much longer.\
        I am so scared of the future, and I feel like I'm the only 22 year old feeling the pressures of taking care of her aging parents while having no money and poor health myself. I don't know what to do. I wish my parents could stay home and take it easy as they deserve... Any advice helps.\
        ",
      ],

      beforeEdit: "",
      inputText: "",

      mimicWriting: "",
      example1: sessionStorage.getItem("example1"),
      example2: sessionStorage.getItem("example2"),
      example3: sessionStorage.getItem("example3"),
      experience: "",
      thought: "",
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
      post: sessionStorage.getItem("main_2"),
    };
  },

  methods: {
    fetchData() {
      console.log("ID: ", this.$route.query);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
      if (this.condition == "5") {
        this.nextPageBool = true;
      }
      this.experience = sessionStorage.getItem("experience_" + this.post);
      this.thought = sessionStorage.getItem("thoughts_" + this.post);
      console.log("eperience", this.experience);
      console.log("though", this.thought);
      console.log("post", this.post);
      // console.log("post", this.example1);
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

          if (this.condition == "5") {
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

      if (this.condition != "5") {
        console.log("getWrtingAssistantHelp");
        this.getWrtingAssistantHelp();
      }
      if (sessionStorage.getItem("main_task_start_" + this.post) === null)
        sessionStorage.setItem("main_task_start_" + this.post, Date.now());
      this.enableOutputEditMode();

      this.addHashToLocation();
    },

    getWrtingAssistantHelp() {
      console.log("currentPost:", this.post);
      prompt = "";
      if (this.condition == "1") {
        prompt = `You will craft a supportive message (1-200 words) mirroring a specific linguistic style. First, I will supply you with several sample messages written by an individual. Your task is to assimilate the linguistic nuances of this individual, focusing on attributes like function words, formality level, positivity, verbosity, and directness. There's no requirement to share the outcomes of your linguistic analysis.\n
                    Formality refers to the extent to which the text is formal. Positivity refers to the extent to which the text carries positive sentiments. Verbosity pertains to the wordiness of the text. Directness refers to the extent to which the text explicitly reveals the writer’s intentions. \n
                    [Writing style sample 1]\n
                     ${this.example1}\n
                     [Writing style sample 2]\n
                     ${this.example2}\n
                     [Writing style sample 3]\n
                     ${this.example3}\n
                     With the absorbed linguistic style in mind, compose a supportive response to the subsequent help-seeking post.  Your response should ideally:\n
                     1. Express emotions such as warmth, compassion, and concern;\n
                     2. Convey understanding and explanation of feelings or experiences of the support seeker;]\n
                     3. Delve deeper into feelings and experiences, even if not directly mentioned. \n
                     [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n `;
      }
      if (this.condition == "2") {
        prompt = `You'll be crafting a supportive message (1-200 words) based on my personal experience. I'll provide a post seeking support, followed by my own related experience.\n
                    [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n 
                    [personal experience]\n
                      ${this.experience}\n
                      Based on my input, please create a supportive message that will:\n
                      1. Express emotions such as warmth, compassion, and concern;\n
                      2. Convey understanding and explanation of feelings or experiences of the support seeker;\n
                      3. Delve deeper into feelings and experiences, even if not directly mentioned. \n
                     `;
      }
      if (this.condition == "3") {
        prompt = `You'll be crafting a supportive message (1-200 words) based on my personal thoughts and feelings. I'll provide a post seeking support, followed by my own thoughts and feelings.\n
                      [help-seeking post]\n
                      ${this.seekingPost[parseInt(this.post) - 1]}\n 
                      [personal thoughts/feelings]\n
                      ${this.thought}\n
                      Based on my input, please create a supportive message that will:\n
                      1. Express emotions such as warmth, compassion, and concern;\n
                      2. Convey understanding and explanation of feelings or experiences of the support seeker;\n
                      3. Delve deeper into feelings and experiences, even if not directly mentioned. \n
                     `;
      }
      if (this.condition == "4") {
        prompt = `${this.Prompt}\n
                     [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n `;
      }
      if (this.condition == "6") {
        prompt = `You'll be crafting a supportive message (1-200 words) based on my input. I'll provide a support-seeking post, followed by my own thoughts, feelings, and experiences.\n
                     [help-seeking post]\n
                     ${this.seekingPost[parseInt(this.post) - 1]}\n 
                     [personal experience]\n
                      ${this.experience}\n
                      [personal thoughts/feelings]\n
                       ${this.thought}\n
                       Based on my input, please create a supportive message that will:\n
                      Express emotions such as warmth, compassion, and concern;\n
                      Convey understanding and explanation of feelings or experiences of the support seeker;\n
                      Delve deeper into feelings and experiences, even if not directly mentioned.`;
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
          if (sessionStorage.getItem("main_task_end_" + this.post) === null)
            sessionStorage.setItem("main_task_end_" + this.post, Date.now());
          console.log("output Text:", res.data);
        })
        .catch((e) => {
          console.log(e);
        });
    },

    humanWritingsubmitWriting() {
      let count = 0;
      for (let i = 0; i < this.text.split(" ").length; i++) {
        if (this.text.split(" ")[i] !== "") {
          count++;
        }
      }
      if (count <= 50) {
        this.messagePop(
          "error",
          "Please provide a writing sample of more than 50 words. The current word count is " +
            count +
            "."
        );
        return;
      }
      this.messagePop(
        "success",
        "Support message submitted. Please fill out the survey below."
      );
      if (sessionStorage.getItem("main_task_end_" + this.post) === null)
        sessionStorage.setItem("main_task_end_" + this.post, Date.now());
      http
        .post("/update_support_message/", {
          pid: this.Pid,
          post: this.post,
          text: this.text,
        })
        .then((res) => {
          this.surveyShow = true;
        })
        .catch((e) => {
          console.log(e);
        });
    },
    submitWriting() {
      if (this.condition == "5") {
        this.$router.push({
          path: "/writing_assitant_show_3",
          query: {
            Pid: this.Pid,
            condition: this.condition,
          },
        });
      } else {
        this.$router.push({
          path: "/edit_writing_2",
          query: {
            Pid: this.Pid,
            condition: this.condition,
          },
        });
      }
    },

    addSurveyListener() {
      window.addEventListener("message", (e) => {
        console.log(e);
        if (
          e.origin.includes("https://nus.syd1.qualtrics.com") &&
          e.data.includes("QualtricsEOS|SV_1RB8EWvsV7a5iFU")
        ) {
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
        "https://nus.syd1.qualtrics.com/jfe/form/SV_1RB8EWvsV7a5iFU" + params;
    },
  },
  updated() {
    if (this.condition == "5") this.gLoading = false;
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


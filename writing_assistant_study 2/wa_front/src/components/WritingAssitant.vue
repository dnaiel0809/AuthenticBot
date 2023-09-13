@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>

    <div
      class="container"
      element-loading-text="Please wait a moment..."
      v-loading.fullscreen.lock="loading"
    >
      <p style="font-size: 1.2rem">
        <br />
        Next, you'll be presented with 3 support-seeking posts from online
        communities. For each post, please craft a supportive response of at
        least 50 words. After completing each response, click "submit" before
        moving to the next post.
      </p>
      <p style="font-size: 1.2rem">
        Note: If your response is random and doesn't align with the
        support-seeking post, it will be rejected.
      </p>
      <!-- task1 -->
      <div id="randomContainer">
        <div
          v-show="order == 1"
          class="translate-container randomItem"
          v-loading="loading"
        >
          <el-row :gutter="20">
            <el-col :span="12">
              <!--output 部分-->
              <div class="grid-content-post2 bg-light">
                <div
                  class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                  data-animation-name=""
                  data-animation-duration="0"
                  data-animation-direction=""
                >
                  <!-- emo -->
                  <h5 style="text-align: left">
                    <span style="font-size: 1.8rem">
                      Subject: I start my new job tomorrow morning and I am
                      terrified
                      <br />
                    </span>
                  </h5>

                  <hr />

                  <p><br /></p>
                  <p style="font-size: 1.2rem">
                    My wife (38) had a stroke that left her with no motor
                    function. She will require care for the rest of her life. We
                    have two little girls. 11 and 8. I need advice on how to
                    protect the estate if anything were to happen to me. I don't
                    want her ongoing care to drain the estate if I'm gone. I
                    also need to set up protection for our kids. I have so many
                    questions about long term disability, social security, etc.
                    I'm overwhelmed and don't know where to begin.
                  </p>
                  <p style="font-size: 1.2rem">
                    The work is of my interest, the hours are to my liking, the
                    pay is more than decent, and even one of my friends works in
                    the office. I am still so, so scared.
                  </p>
                  <p style="font-size: 1.2rem">
                    I have my outfit picked out, and I packed my bag. Dyed my
                    roots and did my nails. I am going to try to eat some dinner
                    now.
                  </p>
                  <p style="font-size: 1.2rem">
                    I've wanted to return to the world of work for so long, and
                    here I am. I would be thrilled if I wasn't so scared.
                  </p>
                  <p><br /><br /><br /></p>
                </div>
              </div>
            </el-col>

            <!-- 核心部件-->
            <el-col :span="12">
              <!-- <el-row :gutter="20"> -->
              <!--input 部分-->
              <div class="grid-content bg-light">
                <label
                  style="
                    font-family: Roboto, RobotoDraft, Helvetica, Arial,
                      sans-serif;
                    font-size: large;
                  "
                  >Write your support message.</label
                >
                <p style="font-size: small; color: grey">
                  Note: You should write at less 50 words.
                </p>
                <textarea
                  id="inputArea1"
                  ref="markdownEditor1"
                  class="textarea"
                ></textarea>
                <el-button
                  @click="submitWriting(markdownEditor1)"
                  type="primary"
                  style="margin-left: 16px; margin-right: 50%"
                  >Submit</el-button
                >
              </div>
            </el-col>
          </el-row>
        </div>
        <!-- task2 -->
        <div
          v-show="order == 2"
          class="translate-container randomItem"
          v-loading="loading"
        >
          <el-row :gutter="20">
            <el-col :span="12">
              <!--output 部分-->
              <div class="grid-content-post2 bg-light">
                <div
                  class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                  data-animation-name=""
                  data-animation-duration="0"
                  data-animation-direction=""
                >
                  <h5 style="text-align: left">
                    <span style="font-size: 1.8rem"
                      >Subject: Caught my girlfriend cheating and I CANNOT cope
                      please help

                      <br />
                    </span>
                  </h5>
                  <hr />
                  <p><br /></p>

                  <p style="font-size: 1.2rem">
                    So long story short I found texts on my(18M) gf(19) phone
                    tonight texting her friend things like “he pounded my shit”
                    “I got some of the best dick last night” and “omg it was so
                    good, I couldn’t walk last night”
                  </p>
                  <p style="font-size: 1.2rem">
                    I’m disgusted. It was her ex, whom I’ve always felt inferior
                    too like she just hadn’t gotten over him even after over a
                    year.
                  </p>
                  <p style="font-size: 1.2rem">
                    She’s REALLY sorry. I saw her crying when she didn’t know I
                    could see her and she was hitting the steering wheel over
                    and over again. I feel bad but like the lying and deception
                    isn’t new. I had to do it. I told her we’re over, but she’s
                    welcome to try to win me back or whatever idc.
                  </p>
                  <p style="font-size: 1.2rem">
                    Part of me just wants to let it slide if she does show
                    effort at getting me back. I know in a while I’ll be ok but
                    I just don’t know how to get from part a to part b.
                  </p>

                  <p style="font-size: 1.2rem">Please help.</p>

                  <p><br /><br /><br /></p>
                </div>
              </div>
            </el-col>

            <!-- 核心部件-->
            <el-col :span="12">
              <!-- <el-row :gutter="20"> -->
              <!--input 部分-->
              <div class="grid-content bg-light">
                <label
                  style="
                    font-family: Roboto, RobotoDraft, Helvetica, Arial,
                      sans-serif;
                    font-size: large;
                  "
                  >Write your support message.</label
                >
                <p style="font-size: small; color: grey">
                  Note: You should write at less 50 words.
                </p>
                <textarea
                  id="inputArea2"
                  ref="markdownEditor2"
                  class="textarea"
                ></textarea>
                <el-button
                  @click="submitWriting(markdownEditor2)"
                  type="primary"
                  style="margin-left: 16px; margin-right: 50%"
                  >Submit</el-button
                >
              </div>
            </el-col>
          </el-row>
        </div>
        <!-- task3  -->
        <div
          v-show="order == 3"
          class="translate-container randomItem"
          v-loading="loading"
        >
          <el-row :gutter="20">
            <el-col :span="12">
              <!--output 部分-->
              <div class="grid-content-post2 bg-light">
                <div
                  class="fr-view u-clearfix u-hover-feature u-rich-text u-text u-text-1"
                  data-animation-name=""
                  data-animation-duration="0"
                  data-animation-direction=""
                >
                  <h5 style="text-align: left">
                    <span style="font-size: 1.8rem">
                      Subject: My wife wants to try for another baby after our
                      sons death

                      <br />
                    </span>
                  </h5>
                  <hr />
                  <p><br /></p>

                  <p   style="font-size: 1.2rem">
                    I have been married to my wife for 8 years. We had a 5year
                    old child, who was terminally ill, and passed in January. We
                    of course took it extremely hard, my wife actually had to be
                    hospitalized. Last month my wife brought up the idea of
                    another baby, saying she couldn’t imagine her life not being
                    a mother. I told her not yet, it was too soon, and she is
                    convinced she is running out of time. She’s been an
                    emotional mess since she first asked, and everytime I turn
                    down the idea, she falls apart and cries. I just feel as if
                    we had a kid right now we wouldn’t be there correctly
                    emotionally, and it’d feel as if we were replacing our son.
                    I hate breaking my wife’s heart and I want to give her
                    everything she wants, but I just think this isn’t the time.
                    Advice?
                  </p>

                  <p><br /><br /><br /></p>
                </div>
              </div>
            </el-col>

            <!-- 核心部件-->
            <el-col :span="12">
              <!-- <el-row :gutter="20"> -->
              <!--input 部分-->
              <div class="grid-content bg-light">
                <label
                  style="
                    font-family: Roboto, RobotoDraft, Helvetica, Arial,
                      sans-serif;
                    font-size: large;
                  "
                  >Write your support message.</label
                >
                <p style="font-size: small; color: grey">
                  Note: You should write at less 50 words.
                </p>
                <textarea
                  id="inputArea3"
                  ref="markdownEditor3"
                  class="textarea"
                ></textarea>
                <el-button
                  @click="submitWriting(markdownEditor3)"
                  type="primary"
                  style="margin-left: 16px; margin-right: 50%"
                  >Submit</el-button
                >
              </div>
            </el-col>
          </el-row>
        </div>
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
import ElementUI from "element-ui";

Vue.use(ElementUI);
// Import Bootstrap and BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);

export default {
  name: "WritingAssitant",
  components: {
    VueMarkdown,
    EasyMDE,
    VueSimpleRangeSlider,
  },

  mounted() {
    this.fetchData();
    this.enableEditMode();
    this.orders = this.shuffleArray(this.orders);
    this.order = this.orders[this.current];
    if (this.order == 1) {
      sessionStorage.setItem("training_start_1", Date.now());
    } else if (this.order == 2) {
      sessionStorage.setItem("training_start_2", Date.now());
    } else if (this.order == 3) {
      sessionStorage.setItem("training_start_3", Date.now());
    }
    // this.enableEditMode();
    // this.enableOutputEditMode();
  },
  data() {
    return {
      Pid: "",
      testData: "",
      edit: false,
      p_edit: false,
      sliderBool: false,
      generateBool: true,
      markdownContent: "",
      prompts: null,
      my_prompts: null,
      drawer: false,
      my_drawer: false,
      direction: "rtl",

      mimicPromptRw:
        "I will provide you with a few messages that a person wrote. You need to identify this person's linguistic style, including function words (ie, auxiliary verbs, articles, common adverbs, personal pronouns, indefinite pronouns, prepositions, negations, conjunctions, and quantifiers) and communication styles (ie, formality, positivity, verbosity, directness).\n\
        Formality refers to the extent to which the text is formal.\n\
        Positivity refers to the extent to which the text carries positive sentiments.\n\
        Verbosity pertains to the wordiness and repetitiveness of written content.\n\
        Directness refers to the extent to which speakers reveal their intentions through explicit communication.\n",

      // Prompt:
      //   "Please write the support message that responses to the help-seeking post including the user’s writing style samples(if provide), attitude (if provide), and experience (if provide).\
      //   Your generate support message should less than 200 words.",

      // PromptRW:
      //   "Write a support message within 200 words in response to the help-seeking post below using the identified functions words and language styles: ",
      // languagePromptRW: "Writing in a conversational and informal tone.",
      // attitudePromptRW: "Incroporating my ture thought: ",
      // experiencePromptRW: "Sharing my experience: ",

      seekingPost:
        "I failed at every aspect of life\n\
        Declining health. couldn't complete my degree. never been in a relationship, lost contact with all my friends. probably gonna get fired from the job soon.\
        I turn 25 this year. I've lived liked this since I was a teenager. I gave up on life before it even started. I could have changed all of this but I didn't. I was too much of a coward to do so. Now its too late.\
        There is nothing to look forward to. I'm never getting married. I can't go visit another country. I'm gonna rot like this until the day that I die.\
        If I don't kms loneliness will. How can one person fuck up this bad? Not just once but multiple times?",

      regenerationPrompt:
        "Adjust the style of the providing paragraph according to three values of the styles.\
        The higher value, the stronger the style effect is. 100 is the max value, and 0 is the minimum value. 50 is neutral.",
      beforeEdit: "",
      inputText: "",
      inputText2: "",
      inputText3: "",

      style: "",
      // models:['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4'],
      models: ["gpt-3.5-turbo", "gpt-3.5-turbo-16k"],
      selectedItem: "gpt-4",

      editMode: true,
      m_outputText: "",
      markdownEditor1: null,
      markdownEditor2: null,
      markdownEditor3: null,

      markdownOutputEditor: null,

      condition: "",
      toAttitudinalBool: false,
      toExperientialBool: false,
      toStyleLearningBool: true,
      loading: false,
      order: 0,
      current: 0,
      orders: [1, 2, 3],
    };
  },

  methods: {
    fetchData() {
      console.log("ID: ", this.$route.query);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
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

    enableEditMode() {
      this.editMode = true;
      const vm = this;
      this.$nextTick(() => {
        if (!this.markdownEditor1) {
          this.markdownEditor1 = new EasyMDE({
            element: this.$refs.markdownEditor1,
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

          this.markdownEditor1.codemirror.on("change", () => {
            vm.inputText = vm.markdownEditor1.value();
            console.log(vm.inputText); // 输出当前的输入值
          });
        }
        if (!this.markdownEditor2) {
          this.markdownEditor2 = new EasyMDE({
            element: this.$refs.markdownEditor2,
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

          this.markdownEditor2.codemirror.on("change", () => {
            vm.inputText2 = vm.markdownEditor2.value();
            console.log(vm.inputText2); // 输出当前的输入值
          });
        }
        if (!this.markdownEditor3) {
          this.markdownEditor3 = new EasyMDE({
            element: this.$refs.markdownEditor3,
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

          this.markdownEditor3.codemirror.on("change", () => {
            vm.inputText3 = vm.markdownEditor3.value();
            console.log(vm.inputText3); // 输出当前的输入值
          });
        }
      });
    },

    enableOutputEditMode() {
      const vm = this;
      this.$nextTick(() => {
        if (!this.markdown) {
          this.markdownOutputEditor = new EasyMDE({
            element: this.$refs.markdownEditorOutput,
          });
          this.markdownOutputEditor.codemirror.setOption("readOnly", true);
          //设计样式
          const codemirrorScroll =
            document.getElementsByClassName("CodeMirror-scroll")[1];
          if (codemirrorScroll) {
            codemirrorScroll.style.maxHeight = "400px";
            codemirrorScroll.style.overflowY = "auto";
            console.log("successfully set");
          }
        }
      });
    },

    submitWriting(markdownEditor) {
      if (markdownEditor == this.markdownEditor1) {
        console.log("markdownEditor1");

        let count = 0;
        for (let i = 0; i < this.inputText.split(" ").length; i++) {
          if (this.inputText.split(" ")[i] !== "") {
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
        sessionStorage.setItem("training_end_1", Date.now());
        this.upLoadText("1", this.inputText);
        sessionStorage.setItem("example1", this.inputText);
        this.messagePop("success", "Support message submitted");
        console.log(markdownEditor.value());
      }
      if (markdownEditor == this.markdownEditor2) {
        console.log("markdownEditor2");
        let count2 = 0;
        for (let i = 0; i < this.inputText2.split(" ").length; i++) {
          if (this.inputText2.split(" ")[i] !== "") {
            count2++;
          }
        }
        if (count2 <= 50) {
          this.messagePop(
            "error",
            "Please provide a writing sample of more than 50 words. The current word count is " +
              count2 +
              "."
          );
          return;
        }
        sessionStorage.setItem("training_end_2", Date.now());
        this.upLoadText("2", this.inputText2);
        sessionStorage.setItem("example2", this.inputText2);
        this.messagePop("success", "Support message submitted");
        console.log(markdownEditor.value());
      }
      if (markdownEditor == this.markdownEditor3) {
        console.log("markdownEditor3");
        let count3 = 0;
        for (let i = 0; i < this.inputText3.split(" ").length; i++) {
          if (this.inputText3.split(" ")[i] !== "") {
            count3++;
          }
        }
        if (count3 <= 50) {
          this.messagePop(
            "error",
            "Please provide a writing sample of more than 50 words. The current word count is " +
              count3 +
              "."
          );
          return;
        }
        sessionStorage.setItem("training_end_3", Date.now());
        this.upLoadText("3", this.inputText3);
        sessionStorage.setItem("example3", this.inputText3);
        console.log(markdownEditor.value());
        this.messagePop("success", "Support message submitted");
      }
      this.current = this.current + 1;
      if (this.current == 3) {
        this.$router.push({
          path: "/writing_assitant_show",
          query: { Pid: this.Pid, condition: this.condition },
        });
      }
      this.order = this.orders[this.current];
      if (this.order == 1) {
        sessionStorage.setItem("training_start_1", Date.now());
      } else if (this.order == 2) {
        sessionStorage.setItem("training_start_2", Date.now());
      } else if (this.order == 3) {
        sessionStorage.setItem("training_start_3", Date.now());
      }
    },

    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
      }
      console.log(array);
      return array;
    },

    upLoadText(numberOfPost, text) {
      http
        .post("/update_training_message/", {
          pid: this.Pid,
          post: numberOfPost,
          text: text,
        })
        .then((res) => {
          console.log("success upload task");
        })
        .catch((e) => {
          console.log(e);
        });
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

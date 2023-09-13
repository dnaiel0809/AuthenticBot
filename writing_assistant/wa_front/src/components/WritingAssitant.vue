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
        Next, you'll be presented with 4 support-seeking posts, individually.
        For each post, please craft a response of at least 50 words. After
        completing each response, click "submit" before moving to the next post.
      </p>
      <p style="font-size: 1.2rem">
        Note: If your response doesn't align with the suport-seeking post, it
        might be rejected.
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
                      Subject: Wife had a stroke. Need to protect family and
                      estate.<br />
                    </span>
                  </h5>

                  <hr />

                  <p><br /></p>
                  <p id="isPasted" style="font-size: 1.2rem">
                    My wife (38) had a stroke that left her with no motor
                    function. She will require care for the rest of her life. We
                    have two little girls. 11 and 8. I need advice on how to
                    protect the estate if anything were to happen to me. I don't
                    want her ongoing care to drain the estate if I'm gone. I
                    also need to set up protection for our kids. I have so many
                    questions about long term disability, social security, etc.
                    I'm overwhelmed and don't know where to begin.
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
                      >Subject: I screamed at my child and I feel horrible

                      <br />
                    </span>
                  </h5>
                  <hr />
                  <p><br /></p>

                  <p id="isPasted" style="font-size: 1.2rem">
                    I tried going to ikea with my almost 2,5yo and it was an
                    absolute disaster. He was running away, almost broke a jar,
                    kept crying hysterically, wasn’t cooperating. I tried gentle
                    parenting in the moment but I just got overwhelmed. So i
                    left my shopping cart, picked him up and went to the car. He
                    had a meltdown the entire car ride. I tried hugging him
                    before but he didn’t want to be touched, I tried explaining
                    to him that I understood he wanted to play but mommy has to
                    pick up a few things in the store and we can continue
                    playing later. He usually understand but this time he wasn’t
                    having any of it. So back to the car ride, I got
                    overstimulated halfway through the ride and shouted at him.
                    He has calmed down now and is currently sleeping as it is
                    his nap time. But I feel so defeated and depleted. I have no
                    life anymore. My little boy is so sweet but very sensitive
                    at the same time. As am I. I usually know how to deal with
                    him but not in moments when I’m under time pressure or I
                    have a lot to do. How do I cope and how do I teach him?
                    Help. Xoxo an overwhelmed mommy who’s feeling very guilty.
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
                      Subject: I’ve wasted so much time being depressed, that
                      I’m depressed about wasting time.

                      <br />
                    </span>
                  </h5>
                  <hr />
                  <p><br /></p>

                  <p id="isPasted" style="font-size: 1.2rem">
                    I can’t imagine how many days I have wasted to being sad and
                    crying and not being able to accomplish the things I need to
                    do. I have responsibilities I have deadlines and none of
                    them seem to matter when I am in these dark episodes. How
                    can you force yourself to do what needs to be done when you
                    feel so hopeless and numb?
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
        <!-- task4  -->
        <div
          v-show="order == 4"
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
                      Subject: I failed a class for the first time. I feel
                      ashamed and depressed.

                      <br />
                    </span>
                  </h5>
                  <hr />
                  <p><br /></p>

                  <p style="font-size: 1.2rem">Greetings,</p>
                  <p style="font-size: 1.2rem">
                    As the title implies, I failed a class and this has brought
                    a lot of shame to myself and depression. I'm considered an
                    intelligent person (I do not say this with the intention of
                    being rude) by my peers around the campus but after
                    receiving the news that I failed a subject (medical
                    sexology), my world fell apart.
                  </p>
                  <p style="font-size: 1.2rem">
                    I do admit that this semester wasn't the greatest since I
                    have a sick mother and I have to take care of her, I was
                    juggling the subjects (metaphorically speaking) to see if I
                    could save them all. Even if I failed one, I feel sick to my
                    stomach.
                  </p>
                  <p style="font-size: 1.2rem">I'm lost and in despair…</p>
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
                  id="inputArea4"
                  ref="markdownEditor4"
                  class="textarea"
                ></textarea>
                <el-button
                  @click="submitWriting(markdownEditor4)"
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
    } else if (this.order == 4) {
      sessionStorage.setItem("training_start_4", Date.now());
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
      inputText4: "",

      style: "",
      // models:['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4'],
      models: ["gpt-3.5-turbo", "gpt-3.5-turbo-16k"],
      selectedItem: "gpt-4",

      editMode: true,
      m_outputText: "",
      markdownEditor1: null,
      markdownEditor2: null,
      markdownEditor3: null,
      markdownEditor4: null,
      markdownOutputEditor: null,

      condition: "",
      toAttitudinalBool: false,
      toExperientialBool: false,
      toStyleLearningBool: true,
      loading: false,
      order: 0,
      current: 0,
      orders: [1, 2, 3, 4],
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
        if (!this.markdownEditor4) {
          this.markdownEditor4 = new EasyMDE({
            element: this.$refs.markdownEditor4,
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

          this.markdownEditor4.codemirror.on("change", () => {
            vm.inputText4 = vm.markdownEditor4.value();
            console.log(vm.inputText4); // 输出当前的输入值
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

          // this.markdownOutputEditor.codemirror.on("change", () => {
          //   // vm.outputText = vm.markdownOutputEditor.value();
          //   //每次 vue-diff 的值也会跟着变
          //   this.$set(this, 'outputText', this.markdownOutputEditor.value());
          //   console.log(vm.outputText); // 输出当前的输入值
          // });
        }
      });
    },

    // async getWrtingAssistantHelp() {
    //   this.loading = true;
    //   let promptInfo = `${this.mimicPromptRw}\n
    //                 [Writing style sample 1]\n
    //                  ${this.inputText}\n
    //                  [Writing style sample 2]\n
    //                  ${this.inputText2}\n
    //                  [Summary]\n `;

    //   console.log("提交的数据是：", promptInfo);
    //   http
    //     .post("/writing_mimic/", {
    //       prompt: promptInfo,
    //       model: this.selectedItem,
    //       user: this.Pid,
    //       info_or_emotional: 2,
    //     })
    //     .then((res) => {
    //       console.log("success", promptInfo);
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });

    //   let promptEmotional = `${this.mimicPromptRw}\n
    //                  [Writing style sample 1]\n
    //                  ${this.inputText3}\n
    //                  [Writing style sample 2]\n
    //                  ${this.inputText4}\n
    //                  [Summary]\n `;
    //   this.messagePop(
    //     "success",
    //     "Take a few seconds to analyze your text. Please wait."
    //   );
    //   console.log("提交的数据是：", promptEmotional);
    //   http
    //     .post("/writing_mimic/", {
    //       prompt: promptEmotional,
    //       model: this.selectedItem,
    //       user: this.Pid,
    //       info_or_emotional: 3,
    //     })
    //     .then((res) => {
    //       this.loading = false;
    //       // this.markdownOutputEditor.value(res.data.content);
    //       this.style = res.data.content;
    //       this.$router.push({
    //         path: "/writing_assitant_show",
    //         query: { Pid: this.Pid, condition: this.condition },
    //       });
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },

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
      if (markdownEditor == this.markdownEditor4) {
        console.log("markdownEditor4");
        let count4 = 0;
        for (let i = 0; i < this.inputText4.split(" ").length; i++) {
          if (this.inputText4.split(" ")[i] !== "") {
            count4++;
          }
        }
        if (count4 <= 50) {
          this.messagePop(
            "error",
            "Please provide a writing sample of more than 50 words. The current word count is " +
              count4 +
              "."
          );
          return;
        }
        sessionStorage.setItem("training_end_4", Date.now());
        this.upLoadText("4", this.inputText4);
        sessionStorage.setItem("example4", this.inputText4);
        console.log(markdownEditor.value());
        this.messagePop("success", "Support message submitted");
      }
      this.current = this.current + 1;
      if (this.current == 4) {
        
        this.$router.push({
          path: "/writing_assitant_show",
          query: { Pid: this.Pid, condition: this.condition },
        });
        // }
      }
      this.order = this.orders[this.current];
      if (this.order == 1) {
        sessionStorage.setItem("training_start_1", Date.now());
      } else if (this.order == 2) {
        sessionStorage.setItem("training_start_2", Date.now());
      } else if (this.order == 3) {
        sessionStorage.setItem("training_start_3", Date.now());
      } else if (this.order == 4) {
        sessionStorage.setItem("training_start_4", Date.now());
      }
    },

    // setOrder() {
    //   http
    //     .post("/get_google_sheet_example/", {
    //       pid: this.Pid,
    //       condition: this.condition,
    //     })
    //     .then((res) => {
          
    //       this.order = [res.data.order1, res.data.order2];
          
    //       sessionStorage.setItem("main_1", this.order[0]);
    //       sessionStorage.setItem("main_2", this.order[1]);
    //       // this.condition = res.data.condition;
    //       console.log("condition:", this.condition);
    //       console.log("order:", this.order);
    //       console.log("order:", this.post);
    //     })
    //     .catch((e) => {
    //       console.log(e);
    //     });
    // },

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

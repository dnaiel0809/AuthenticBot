@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>
    <div class="container">
      <div v-show="condition == 2">
        <p style="font-size: 1.2rem">
          This is the third post. Answer the question regarding the post.
        </p>
      </div>
      <div v-show="condition == 3">
        <p style="font-size: 1.2rem">
          This is the third post. Answer the question regarding the post.
        </p>
      </div>
      <div v-show="condition == 6">
        <p style="font-size: 1.2rem">
          This is the first post. Instead of writing a supportive message, you
          are expected to share personal experiences, thoughts, and feelings
          related to the poster and their situation.
        </p>
      </div>
      <!-- <p style="font-size: 1.2rem">
        You can now revise the message as needed. Feel free to make any changes
        if you see fit. Once you're happy with your response, kindly fill out
        the survey. The message will be saved and uploaded automatically. Note
        that this support message will be shared anonymously in an online peer
        support community.
      </p> -->
      <!-- <p>After you submit, you'll be asked to evaluate your written message.</p> -->

      <el-row :gutter="20">
        <el-col :span="12">
          <div>
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
          <div class="grid-content bg-light">
            <div class="label_container" style="display: flex">
              <label
                style="
                  font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                  font-size: large;
                "
              ></label>
            </div>
            <div v-show="condition == 2 || condition == 6">
              <p style="font-size: 1.2rem">
                <!-- Have you ever experienced a similar situation that you'd like to
                share? If yes, please briefly describe your experience. If not,
                you can just say that you don’t have similar experiences. -->
                Your experience:
              </p>
              <textarea
                id="outputArea"
                ref="markdownEditor"
                class="textarea"
              ></textarea>
            </div>
            <div v-show="condition == 3 || condition == 6">
              <p style="font-size: 1.2rem">
                <!-- What are your thoughts and feelings on this matter,
                regardless of what the other person may want to hear? -->
                Your thoughts and feelings:
              </p>
              <textarea
                id="outputArea2"
                ref="markdownEditor2"
                class="textarea"
              ></textarea>
            </div>
          </div>
          <el-button
            @click="nextpage"
            type="primary"
            style="margin: 10px"
            v-show="nextPageBool"
            >Submit</el-button
          >
        </el-col>
      </el-row>
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
  name: "Question_3",
  components: { EasyMDE },

  mounted() {
    this.fetchData();
    this.enableEditMode();
    // this.cannotGoback();
    this.scrollToTop();
  },
  data() {
    return {
      text: "",
      text2: "",
      Pid: "",
      nextPageBool: true,
      condition: "",
      post: sessionStorage.getItem("main_3"),
      serveyBool: false,
      markdownEditor: null,
      markdownEditor2: null,
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
      if (sessionStorage.getItem("question_start_" + this.post) === null)
        sessionStorage.setItem("question_start_" + this.post, Date.now());
      console.log(this.post);
    },
    enableEditMode() {
      this.editMode = true;
      const vm = this;
      this.$nextTick(() => {
        if (!this.markdownEditor && (this.condition == "2"||this.condition == "6")) {
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
          this.markdownEditor.codemirror.on("change", () => {
            vm.text = vm.markdownEditor.value();
            console.log(vm.text); // 输出当前的输入值
          });
        }
        if (!this.markdownEditor2 && (this.condition == "3"||this.condition == "6")) {
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
            vm.text2 = vm.markdownEditor2.value();
            console.log(vm.text2); // 输出当前的输入值
          });
        }
      });
    },
    async submitWriting() {
      if (this.text == "" && (this.condition == "2"||this.condition == "6")) this.text = "NA";
      if (this.text2 == "" && (this.condition == "3"||this.condition == "6")) this.text2 = "NA";
      sessionStorage.setItem("experience_" + this.post, this.text);
      sessionStorage.setItem("thoughts_" + this.post, this.text2);
      if (sessionStorage.getItem("question_end_" + this.post) === null)
        sessionStorage.setItem("question_end_" + this.post, Date.now());
      await new Promise((r) => setTimeout(r, 2000));
      http
        .post("/upload_experience_thoughts_task/", {
          pid: this.Pid,
          post: this.post,
          exprience: this.text,
          thought: this.text2,
        })
        .then((res) => {
          console.log("success", res.data.success);
          this.messagePop("success", "Successfully submit!");
          this.jumpyTo("/writing_assitant_show_3");
        })
        .catch((e) => {
          console.log(e);
        });
    },
    nextpage() {
      this.submitWriting();
      this.nextPageBool = false;
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

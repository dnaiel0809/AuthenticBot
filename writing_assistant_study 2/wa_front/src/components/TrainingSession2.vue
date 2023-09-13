@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');


<template>
  <div>
    <header class="header-slot">
      <slot name="header"><h4>Support message web</h4></slot>
    </header>

    <div class="container">
      <div class="bg-light">
        <h4>What is Supportive Communication?</h4>
        <ul>
          <li style="font-size: 1.2rem">
            It involves both verbal and non-verbal actions to assist those
            seeking help.
          </li>
          <li style="font-size: 1.2rem">Supportive messages often offer:</li>
          <ul>
            <li style="font-size: 1.2rem">
              Emotional Support: Understanding, reassurance, encouragement, etc.
            </li>
            <li style="font-size: 1.2rem">
              Informational Support: Advice, sharing resources, etc.
            </li>
          </ul>
        </ul>
        <!-- <p><br /></p> -->
        <h4>The Role of Empathy in Supportive Messages:</h4>
        <p style="font-size: 1.2rem">
          Empathy is central to supportive communication. It's the capacity to
          understand or feel the emotions and experiences of others and express
          that understanding in responses. In essence, empathy lets you walk in
          someone else's shoes.
        </p>
        <p style="font-size: 1.2rem">Empathetic response typically involve:</p>
        <ol>
          <li style="font-size: 1.2rem">
            Knowing: Recognizing someone's emotions and experiences.
          </li>
          <li style="font-size: 1.2rem">
            Feeling: Resonating with those emotions.
          </li>
          <li style="font-size: 1.2rem">
            Responding: Offering compassionate reactions based on the
            understanding.
          </li>
        </ol>
        <h4>Crafting Empathic Responses:</h4>
        <p style="font-size: 1.2rem">A good empathic response might include:</p>
        <ul>
          <li style="font-size: 1.2rem">
            <b>Emotional reactions</b>: Express emotions such as warmth,
            compassion, and concern (e.g., “I’m sorry to hear this”).
          </li>
          <li style="font-size: 1.2rem">
            <b>Interpretations</b>: Convey understanding and explanation of
            feelings or experiences (e.g., "It must be really terrifying for
            you").
          </li>
          <li style="font-size: 1.2rem">
            <b>Explorations</b> Delve deeper into feelings and experiences, even
            if not directly mentioned (e.g., "Are you feeling isolated
            currently?").
          </li>
        </ul>
        <h4>Example:</h4>
        <p style="font-size: 1.2rem">
          Support-seeking post: "Lately, I've been struggling with my bipolar
          disorder. I feel like I'm on a roller coaster that I can't get off.
          I'm scared and unsure of how to manage."
        </p>
        <p style="font-size: 1.2rem">
          Empathic Response: “I'm really sorry to hear you're going through
          this. It must be so tough managing such intense mood fluctuations.
          Have there been any strategies or treatments that have provided some
          relief before?"
        </p>

        <p style="font-size: 1.2rem">
          Not Empathic Response: "Everything will be alright. You might be
          overthinking it. Just try harder to cope."
        </p>
      </div>
      <center>
        <el-button
          :disabled="isDisabled"
          @click="nextpage"
          type="primary"
          style="margin: 16px"
          >{{ countDown }}</el-button
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

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);

export default {
  name: "TrainingSession2",
  components: { EasyMDE },

  mounted() {
    this.fetchData();
    // this.cannotGoback();
    this.scrollToTop();
    this.countDownTimer();
  },
  data() {
    return {
      text: "",
      currentTask: 0,
      Pid: "",
      loading: true,
      condition: "",
      countDown: 30,
      isDisabled: true,
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
      console.log("Params: ", this.$route.query.Pid);
      this.Pid = this.$route.query.Pid;
      this.condition = this.$route.query.condition;
    },

    nextpage() {
      this.jumpyTo("/writing_assistant");
    },
    countDownTimer() {
      if (this.countDown > 0) {
        setTimeout(() => {
          this.countDown -= 1;
          this.countDownTimer();
          if (this.countDown < 1) {
            this.isDisabled = false;
            this.countDown = "Next Page";
          }
        }, 1000);
      }
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

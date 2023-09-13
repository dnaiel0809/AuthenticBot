<template>
  <div class="container">
    <el-card class="box-card">
      <p>v22</p>
      <!-- <div slot="header" class="clearfix"> -->
      <!--        <span>Login</span>-->
      <!-- <img src="/imgs/ai4sg_logo.png" alt="Logo" class="logo"> -->
      <!-- </div> -->
      <el-form :model="form" label-width="120px">
        <el-form-item label="Prolific ID">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <!-- <el-form-item label="condition">
          <el-input v-model="form.condition"></el-input>
        </el-form-item> -->
        <!-- <el-form-item label="Password">
          <el-input type="password" v-model="form.password"></el-input>
        </el-form-item> -->
        <div class="button">
          <el-button type="primary" @click="signUp">Login</el-button>
        </div>
        <!-- <el-button type="primary" @click="signUp">Sign Up</el-button> -->
      </el-form>
    </el-card>
  </div>
</template>
<script src="https://apis.google.com/js/platform.js?onload=onLoadCallback"></script>

<script>
import http from "@/http";
import VueGAPI from "vue-gapi";

// import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      form: {
        username: "",
        condition: "",
        // password: '',
      },

      randomCondition: this.shuffleArray(["1", "4", "5", "6"]),
    };
  },
  methods: {
    messagePop(type, message) {
      this.$message({
        message: `${message}`,
        type: `${type}`,
      });
    },
    jumpyTo(url) {
      if (this.$router.currentRoute.path !== url) {
        console.log(this.username);
        this.$router.push({
          path: url,
          query: { Pid: this.username, condition: this.condition },
        });
      }
    },
    fetchID() {
      // Get the value of the 'PROLIFIC_PID' parameter from the current URL
      const urlParams = new URLSearchParams(window.location.search);
      this.Pid = urlParams.get("PROLIFIC_PID");
      console.log("ID: ", this.Pid);

      // const [hash, query] = url.split('#')[1].split('?')
      // const params = Object.fromEntries(new URLSearchParams(query))
      // this.Pid = params.PROLIFIC_PID;
      // this.Pid = this.$route.query.PROLIFIC_PID;
      // Update the 'username' variable with the value of 'PROLIFIC_PID'

      this.form.username = this.Pid;
    },

    async signUp() {
      console.log(this.form);
      console.log(this.form.username);
      this.username = this.form.username;
      this.condition = this.randomCondition[0];
      console.log(this.randomCondition);
      // this.condition = this.form.condition;
      // if (
      //       this.condition == "1" ||
      //       this.condition == "2" ||
      //       this.condition == "3" ||
      //       this.condition == "4" ||
      //       this.condition == "5"
      //     ) {

      //     } else {
      //       this.messagePop("error", "condition should be 1~5");
      //       return;
      //     }
      await http
        .post("/signup/", {
          name: this.form.username,
          condition: this.condition,
          // pwd: this.form.password,
        })
        .then((res) => {
          console.log("successfully sign up");
          console.log(res);
          if (res.data.success) {
            this.messagePop("success", "successfully sign up");
            sessionStorage.setItem("main_1", res.data.order1);
            sessionStorage.setItem("main_2", res.data.order2);
            sessionStorage.setItem("main_3", res.data.order3);
            sessionStorage.setItem("username", this.form.username);

            // this.condition = res.data.condition;

            this.jumpyTo("/pre_survey");
          } else {
            this.messagePop("error", "please try another username");
          }
        })
        .catch((e) => {
          console.log("sign up error", e);
          this.messagePop("error", "please try another username");
        });
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
      }
      return array;
    },
  },

  beforeMount() {
    this.fetchID();
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.box-card {
  width: 30%;
}

.logo {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 20%;
}

.button {
  display: block;
  margin-left: auto;
  /* margin-right: auto; */
  width: 20%;
}
</style>
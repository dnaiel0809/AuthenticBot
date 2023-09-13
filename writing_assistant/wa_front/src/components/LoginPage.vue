<template>
  <div class="container">
    <el-card class="box-card">
      <!-- <div slot="header" class="clearfix"> -->
      <!--        <span>Login</span>-->
      <!-- <img src="/imgs/ai4sg_logo.png" alt="Logo" class="logo"> -->
      <!-- </div> -->
      <el-form :model="form" label-width="120px">
        <el-form-item label="Prolific ID">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
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
import VueGAPI from "vue-gapi"

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

    

    // login() {
    //   // Handle login logic here
    //   // console.log(this.form);
    //   http.post('/login/',{
    //     name: this.form.username,
    //     pwd: this.form.password,
    //   }).then(res => {
    //     console.log('successfully login')
    //     console.log(res)
    //     sessionStorage.setItem('username', this.form.username)
    //     this.messagePop('success', "successfully login!!")
    //     this.jumpyTo("/writing_assistant")
    //   //  同时也可以在后端为 single_fileupload 创建一个文件夹
    //   //  后面还可以再后端为 multiple_fileupload 创建一个文件夹

    //   }).catch(e=>{
    //     console.log("login", e)
    //     this.messagePop('error', "login error, wrong username or password")
    //   })
    // },

    async signUp() {
      console.log(this.form);
      console.log(this.form.username);
      this.username = this.form.username;
      await http
        .post("/signup/", {
          name: this.form.username,
          // pwd: this.form.password,
        })
        .then((res) => {
          console.log("successfully sign up");
          console.log(res);
          if (res.data.success) {
            this.messagePop("success", "successfully sign up");
            sessionStorage.setItem("main_1", res.data.order1);
            sessionStorage.setItem("main_2", res.data.order2);
            sessionStorage.setItem("username", this.form.username);
            
            this.condition = res.data.condition;
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
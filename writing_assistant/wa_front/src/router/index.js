/* eslint-disable */
import VueRouter from 'vue-router'
import WritingAssitant from "@/components/WritingAssitant";
import LoginPage from "@/components/LoginPage";
import PostSurvey from "@/components/PostSurvey";
import EditWriting from "@/components/EditWriting";
import EditWriting2 from "@/components/EditWriting_2";
import WritingAssitantShow from "@/components/WritingAssitantShow";
import WritingAssitantShow2 from "@/components/WritingAssitantShow_2";
import PreSurvey from "@/components/PreSurvey";
import TrainingSession from "@/components/TrainingSession";
import TrainingSession2 from "@/components/TrainingSession2";
import Screening from "@/components/Screening";





const router = new VueRouter({
    routes: [{
        path: "/",
        component: LoginPage
    },
    {
        path: "/login",
        component: LoginPage
    },

    {
        path: "/writing_assistant",
        component: WritingAssitant
    },

    {
        path: "/post_survey",
        component: PostSurvey
    },
    {
        path: "/edit_writing",
        // name: 'edit_writing',
        component: EditWriting
    },
    {
        path: "/edit_writing_2",
        component: EditWriting2
    },
    {
        path: "/writing_assitant_show",
        component: WritingAssitantShow
    },
    {
        path: "/writing_assitant_show_2",
        component: WritingAssitantShow2
    },
    {
        path: "/pre_survey",
        component: PreSurvey
    },
    {
        path: "/training_session",
        component: TrainingSession
    },
    {
        path: "/training_session_2",
        component: TrainingSession2
    },
    {
        path: "/screening",
        component: Screening
    },



    ]
});

//路由守卫，守卫 writing_assistant
router.beforeEach((to, from, next) => {
    if (to.path === '/writing_assistant') {   // 如果即将进入的是 '/writing_assistant' 路由
        const sessionData = sessionStorage.getItem('username');   // 通过 'yourItem' 取得 sessionStorage 中的项

        if (!sessionData) {   // 如果该项不存在
            next('/login');   // 重定向到登录页面
        } else {   // 如果该项存在
            next();   // 正常跳转
        }
    } else {   // 对于其它路由
        next();   // 总是允许正常跳转
    }
});

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch((err) => err)
}



export default router;
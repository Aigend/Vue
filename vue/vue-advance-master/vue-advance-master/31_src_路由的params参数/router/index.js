//该文件专门用于创建整个应用的路由器

import VueRouter from "vue-router";
import About from "@/pages/About";
import Home from '@/pages/Home';
import News from "@/pages/News";
import Message from "@/pages/Message";
import Detail from "@/pages/Detail";

//创建并默认暴露一个路由器
export default new VueRouter({
   routes:[
       {
           name: 'regard',
           path:'/about',
           component: About
       },
       {
           path:'/home',
           component: Home,
           children:[
               {
                   path: 'news',
                   component: News
               },
               {
                   path: 'message',
                   component: Message,
                   children:[
                       {
                           name: 'particulars',
                           //node js 中的占位符，params参数必须要使用
                           path: 'detail/:id/:title',
                           component: Detail
                       }
                   ],
               }
           ]
       }
   ]
});


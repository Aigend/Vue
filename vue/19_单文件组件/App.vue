<template>
<!--  组件的结构，如果VSCode没有高亮显示代码，就安装Vetur插件，能显示.vue文件-->
   <div>
     <School></School>
     <Student></Student>
   </div>
</template>

<script>
import School from './School';
import Student from "./Student";

export default {
  name: "App",
  //汇总所有的组件
  components:{
    Student,
    School
  }
}
</script>


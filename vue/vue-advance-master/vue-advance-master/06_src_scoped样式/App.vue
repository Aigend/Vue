<template>
   <div>
     <h1 class="title">你好啊！！！</h1>
      <Student/>
      <hr/>
      <School/>
   </div>
</template>

<script>
// 2个组件中的样式类名冲突，如果没有scoped，采用的是最后引入的一个
import Student from "@/components/Student";
import School from "@/components/School";
export default {
  name: "App",
  components:{
    School,
    Student,
  },
}
</script>

<style>
   /*
   这里不适合加scoped，任何一个组件class加了title,最后都会采用
   全局的样式是不需要加scoped
   全局共享
   */
   .title{
     /* color 字体颜色 */
     color: red;
   }
</style>



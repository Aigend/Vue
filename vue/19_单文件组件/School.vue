<template>
<!--  组件的结构，如果VSCode没有高亮显示代码，就安装Vetur插件，能显示.vue文件-->
   <div class="demo">
     <h2>学校名称:{{ name }}</h2>
     <h2>学校地址:{{ address }}</h2>
     <button @click="showName">点我提示学校名</button>
   </div>
</template>

<style>
  /*css样式,样式的注释，html的注释，js的注释有些差异*/
  .demo{
    background: skyblue;
  }
</style>


<script>
  //组件交互的代码
  //export default school
  export default {
    name: 'School', //开发者工具最终呈现的名字为School
    data(){
      return {
        name:'武汉科技大学',
        address: '武汉'
      }
    },
    methods:{
      showName(){
        alert(this.name);
      }
    }
  };
//这里如果不熟悉，就去补充下ES6的模块化编程
  //统一暴露
  // export { school };
  // export default school //默认暴露
  // 分别暴露
  // export const school = Vue.extend({})
</script>
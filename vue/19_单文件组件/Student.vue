<template>
<!--  组件的结构，如果VSCode没有高亮显示代码，就安装Vetur插件，能显示.vue文件-->
   <div>
     <h2>学生姓名:{{ name }}</h2>
     <h2>学生年龄:{{ age }}</h2>
     <button @click="showName">点我提示学生姓名</button>
   </div>
</template>

<!--<style>-->
<!--  /*css样式*/-->
<!--  .demo{-->
<!--    background: skyblue;-->
<!--  }-->
<!--</style>-->


<script>
  //组件交互的代码
  //export default school分别暴露
  export default {
    name: 'Student', //开发者工具最终呈现的名字为School
    data(){
      return {
        name:'panyue',
        age:21
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
</script>

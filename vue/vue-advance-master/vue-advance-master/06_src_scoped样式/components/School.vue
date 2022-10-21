<template>
   <div class="demo">
     <h2>学校名称:{{  name }}</h2>
     <h2>学校地址: {{ address }}</h2>
   </div>
</template>

<script>
export default {
  name: "School",
  data(){
    console.log(this);
    return {
       name: 'wust university',
       address: '武汉科技大学'
    }
  },
}
</script>

<style scoped>
   /* 不同组件中的样
   式最后是汇总到一起的，如果类名冲突，采用的最后引入的，可以看下App.vue，2个组件引入的先后顺序造成的效果 */
   /*scoped代表局部的*/

  /*
    1.lang 不写默认为css
    2.写less会报错，脚手架没有安装，会报错；安装(要注意版本匹配):npm i less-loader
    查看less-loader服务器版本：npm view less-loader versions
    3.less 格式的css可以嵌套着写样式的格式
    <style lang="less">
      .demo{
        background: orange;
      }
    </style> 
  */
  .demo{
    background: skyblue;
  }
</style>



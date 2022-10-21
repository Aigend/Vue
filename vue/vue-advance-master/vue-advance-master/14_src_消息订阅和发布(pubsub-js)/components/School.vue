<template>
   <div class="demo">
     <h2>学校名称:{{  name }}</h2>
     <h2>学校地址: {{ address }}</h2>
   </div>
</template>

<script>
//安装npm i pubsub-js 当然也可以安装其他库去实现发布订阅这种功能，支持的库不止一种

import pubsub from 'pubsub-js';
export default {
  name: "School",
  data(){
    console.log(this);
    return {
       name: 'wust university',
       address: '武汉科技大学'
    }
  },
  mounted() {
    // console.log('School', this);
    // this.$bus.$on('hello', (data) => {
    //   console.log(`我是School组件,我收到了数据,${data}`);
    // })
    //订阅消息 隔空对讲机喊话

    //第一种写法错误，写成function 函数，this出现问题
    // this.pubId = pubsub.subscribe('hello',  function (name, msg){
    //   //不写成箭头函数，这里的this是undefine
    //   console.log(`有人发布了hello消息，回调被执行,data: ${msg}`);
    // });

    //第二种写法正确，写成箭头函数，但第一个参数为传入的消息名称，其实没必要但是要占位置
    this.pubId = pubsub.subscribe('hello',  (name, msg) => {
      //注意这里写剪头函数this才不会丢，这里的this 是vc
      console.log(`有人发布了hello消息，回调被执行,data: ${msg}`);
    });

    //第三种写法正确，直接传methods中的回调函数，有this 指针的变化过程，但第一个参数还是订阅消息名
    // this.pubId = pubsub.subscribe("hello", this.demo);

  },
  beforeDestroy() {
    // this.$bus.$off('hello'); //销毁解绑
    //取消订阅
    pubsub.unsubscribe(this.pubId); //取消订阅
  }
}
</script>

<style scoped>
   /*scoped代表局部的*/
  .demo{
    background: skyblue;
    padding:5px
  }
</style>



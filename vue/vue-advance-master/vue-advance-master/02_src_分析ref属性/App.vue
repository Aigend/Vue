<template>
   <div>
     <h1 v-text="msg" ref="title"></h1>
     <!-- <button ref="btn" @click="showH">点我输出上方的dom元素</button> -->
     <button @click="showH">点我输出上方的dom元素</button>
     <!-- <School id="sch"/> -->
     <School ref="sch"/>
   </div>
</template>

<script>
import School from "./components/School";
import School from './components/School.vue';
import School from './components/School.vue';

export default {
  name: "App",
  data(){
    return {
      msg: '欢迎学习Vue',
    }
  },
  methods:{
    showH(e){
       // console.log(this.$refs);//是个对象 
      console.log(this.$refs.title); //this ==> vc(app组件)

      console.log(e.target); //发生事件的dom元素m

      // console.log(document.getElementById("sch"))//获取的是完整的dom结构 
      console.log(this.$refs.sch); //可以是school组件加refs属性 获得的是组件事例对象vc
    }
  },
  components:{
    School,
  },
}
</script>


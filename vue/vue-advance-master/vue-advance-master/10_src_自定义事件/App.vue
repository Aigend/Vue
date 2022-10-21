<template>
   <div class="app">
      <h1>{{ msg }},学生姓名是:{{ studentName }}</h1>
      <!--通过绑定一个自定义事件实现了子给父传递数据(自定义事件绑在子组件上) 第一种写法使用@或v-on-->
      <!--once代表改事件只执行一次-->
      <!--<Student @personalEvent="getStudentName" @demo="demo"/>-->
      <!--第二种写法使用ref绑定事件--->
      <Student ref="student" @click.native="show"/>
      <!-- 补充：组件不能按照下面这样绑定原生事件，否则人家就认为是自定义事件，需要组件触发才行-->
      <!-- 这里也可以理解为什么组件模板为什么不让写2个根元素，不然这里的原生绑定事件不知道该给哪个div -->
      <!-- <Student ref="student" @click="show"/> -->
      <!--通过父组件给子组件传递函数类型的props实现了子给父传递数据-->
      <School :getSchoolName="getSchoolName"/>
   </div>
</template>

<script>
import Student from "@/components/Student";
import School from "@/components/School";
export default {
  name: "App",
  components:{
    School,
    Student,
  },
  data(){
    return {
      msg: 'helloこんにちは',
      studentName:''
    }
  },
  methods:{
    getSchoolName(name){
      console.log(`app收到了学校名,${name}`);
    },
    getStudentName(name, ...params){
      console.log('自定义');
      console.log(`app收到了学生名, ${name}`);
      this.studentName = name;//子组件传过来的
      console.log(`剩余参数,${params}`);
    },
    demo(){
      console.log('demo事件被触发了');
    },
    show(){
      console.log(`123`);
    }
  },
  mounted() {
    //可以通过ref拿到组件实例对象
    // setTimeout(() => {
    //   this.$refs.student.$on('personalEvent', this.getStudentName); //当App组件一挂载完毕经过三秒我就在Student组件上绑定事件
    //   //this.$refs.student.$once('personalEvent', this.getStudentName); //注意此时事件只执行一次就不执行了(once),一次性
    // },3000)

    /**
     * 补充：this.$refs.student.$on("atguigu",this.getStudentName)//此处的this,值的是vc app
     * 这里this 是因为有一个this 的转变，从vc student 到 vc app，因为Vue 规定methods中的this是当前的vc对象
    */
    /**
     * this.$refs.student.$on("atguigu",function(name, ...params){console.log(this)})
     * 这里有问题，这里function中的this 发生了改变,是触发事情的实例对象，指的是vc student
     * Vue设计谁触发了绑定事情，回调函数中的this就是谁，这里是vc student
     */
    
    //注意这里回调要写成剪头函数，不然this会丢失,箭头函数这里this是(vc)app,而不是(vc)student
    this.$refs.student.$on('personalEvent', (name) => {
      //箭头函数没有this,会往外找this对象，找mounted中的this 对象
       console.log(this);
       console.log(name);
       this.studentName = name;
    });
  }
}
</script>

<style>
   /*
   全局的样式是不需要加scoped
   全局共享
   */
   .app{
     background: gray;
     padding: 5px;
   }
</style>



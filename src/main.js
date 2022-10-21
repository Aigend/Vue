import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  // render(createElement){
//    return createElement("h1", "你好啊")
  // }
  // template:<h1>你好啊</h1>
  // components:{App}
}).$mount('#app')

//引入Vue
import Vue from "vue";
//引入App
import App from './App';

//引入插件
import plugins from './plugins';

//关闭Vue的生产提示
Vue.config.productionTip = false;

Vue.use(plugins); //vue应用插件
// Vue.use(plugins,x,y,z); //vue应用插件,给插件传参数
new Vue({
    el:'#app',
    render: h => h(App)
});



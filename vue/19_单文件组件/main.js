//创建vm
//这里如果不熟悉，就去补充下ES6的模块化编程
import App from './App';
//如果文件
new Vue({
    el: '#root',
    template:`<App></App>`,
    components:{
        App
    }
});


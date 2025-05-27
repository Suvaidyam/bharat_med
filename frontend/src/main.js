import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import { session } from './Service/auth.js'


import {
  Button,
  Card,
  Input,
  setConfig,
  frappeRequest,
  resourcesPlugin,
} from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)
// app.use(Vue3Toastify, {
//   position: 'top-right',
//   autoClose: 5000,
//   hideProgressBar: false,
//   closeOnClick: true,
//   pauseOnHover: true,
//   draggable: true,
// })


app.provide('$session', session)
app.use(router)
app.use(resourcesPlugin)

app.component('Button', Button)
app.component('Card', Card)
app.component('Input', Input)

app.mount('#app')

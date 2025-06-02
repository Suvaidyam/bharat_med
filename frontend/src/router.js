import { createRouter, createWebHistory } from 'vue-router'
import { session } from './Service/auth.js'
import { userResource } from '@/Service/user.js'
import Dashboard from './pages/Dashboard.vue'
import Admindash from './pages/Admindash.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    name: 'Login',
    path: '/login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    name: 'Register',
    path: '/register',
    component: () => import('@/pages/Register.vue'),
  },
  {
    name: 'FAQs',
    path: '/faqs',
    component: () => import('@/pages/FAQs.vue'),
  },
  // {
  //   name:'Dashboard',
  //   path: '/dashboard',
  //   component: () => import('@/pages/Dashboard.vue'),
  // },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [{
      path: 'admindash',
      name: 'Admindash',
      component: Admindash,
    },
    {
      path: 'doctordash',
      name: 'Doctordash',
      component: () => import('@/pages/Doctordash.vue'),
    },
    {
      path: 'patient',
      name: 'Patient',
      component: () => import('@/pages/Patient.vue'),
    },
    {
      name: 'Addpatientviewlist',
      path: '/addpatientviewlist',
      component: () => import('@/pages/Addpatientviewlist.vue'),
    },
    {
      name: 'Addpatient',
      path: '/addpatient',
      component: () => import('@/pages/Addpatient.vue'),
    },

  ]
  },
  // {
  //   name: 'Patient',
  //   path: '/patient',
  //   component: () => import('@/pages/Patient.vue'),
  // },

  {
    name: 'Log',
    path: '/log',
    component: () => import('@/pages/Auth/Log.vue'),
  },
  {
    name: 'Otp',
    path: '/otp',
    component: () => import('@/pages/Auth/Otp.vue'),
  },
  // {
  //   name: 'Admindash',
  //   path: '/admindash',
  //   component: () => import('@/pages/Admindash.vue'),
  // }
  ,
 
 


]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }
  console.log(to.name,'to.name');
  
  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next()
  } else {
    next()
  }
})

export default router

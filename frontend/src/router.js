import { createRouter, createWebHistory } from 'vue-router'
import { session } from './Service/auth.js'
import { userResource } from '@/Service/user.js'


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
  {
    name:'Dashboard',
    path: '/dashboard',
    component: () => import('@/pages/Dashboard.vue'),
  },{
    name: 'Patient',
    path: '/patient',
    component: () => import('@/pages/Patient.vue'),
  },
  {
    name: 'Design',
    path: '/design',
    component: () => import('@/pages/Design.vue'),
  }
  // {
  //   name: 'Test',
  //   path: '/test',
  //   component: () => import('@/pages/Test.vue'),
  // }
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

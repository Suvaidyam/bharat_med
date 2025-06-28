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
    {
      name: 'Doctorlist',
      path: '/doctorlist',
      component: () => import('@/pages/Doctors/Doctorlist.vue'),
    },
    {
      name: 'Adddoctor',
      path: '/adddoctor',
      component: () => import('@/pages/Doctors/Adddoctor.vue'),
    },
    {
      name: 'Doctorschedule',
      path: '/doctorschedule',
      component: () => import('@/pages/Doctors/Doctorschedule.vue'),
    },
    {
      name: 'Specializations',
      path: '/specializations',
      component: () => import('@/pages/Doctors/Specializations.vue'),
    },
    {
      name: 'Allappointments',
      path: '/allappointments',
      component: () => import('@/pages/Appointment/Allappointments.vue'),
    },
    {
      name: 'Addappointment',
      path: '/addappointments',
      component: () => import('@/pages/Appointment/Addappointment.vue'),
    },
    {
      name: 'Callendar',
      path: '/callendar',
      component: () => import('@/pages/Appointment/Callendar.vue'),
    },
    {
      name: 'Appointmentrequests',
      path: '/appointmentrequests',
      component: () => import('@/pages/Appointment/Appointmentrequests.vue'),
    },
    {
      name: 'Allstaff',
      path: '/allstaff',
      component: () => import('@/pages/Staff/Allstaff.vue'),
    },
    {
      name: 'Addstaff',
      path: '/addstaff',
      component: () => import('@/pages/Staff/Addstaff.vue'),
    },
    {
      name: 'Role',
      path: '/role',
      component: () => import('@/pages/Staff/Role.vue'),
    },
    {
      name: 'Attendance',
      path: '/attendance',
      component: () => import('@/pages/Staff/Attendance.vue'),
    },
    {
      name: 'Pharmacy',
      path: '/pharmacy',
      component: () => import('@/pages/Pharmacy/Pharmacy.vue'),
    },
    {
      name: 'Bloodstock',
      path: '/bloodstock',
      component: () => import('@/pages/Blood Bank/Bloodstock.vue'),
    },
    {
      name: 'Blooddonor',
      path: '/blooddonor',
      component: () => import('@/pages/Blood Bank/Blooddonor.vue'),
    },
    {
      name: 'Bloodissued',
      path: '/bloodissued',
      component: () => import('@/pages/Blood Bank/Bloodissued.vue'),
    },
    {
      name: 'Addbloodunit',
      path: '/addbloodunit',
      component: () => import('@/pages/Blood Bank/Addbloodunit.vue'),
    },
    {
      name: 'Issueblood',
      path: '/issueblood',
      component: () => import('@/pages/Blood Bank/Issueblood.vue'),
    },
    {
      name: 'Invoicelist',
      path: '/invoicelist',
      component: () => import('@/pages/Billing/Invoicelist.vue'),
    },
    {
      name: 'Createinvoice',
      path: '/createinvoice',
      component: () => import('@/pages/Billing/Createinvoice.vue'),
    },
    {
      name: 'Paymenthistory',
      path: '/paymenthistory',
      component: () => import('@/pages/Billing/Paymenthistory.vue'),
    },
    {
      name: 'Insuranceclaims',
      path: '/insuranceclaims',
      component: () => import('@/pages/Billing/Insuranceclaims.vue'),
    },
    {
      name: 'Departmentlist',
      path: '/departmentlist',
      component: () => import('@/pages/Departments/Departmentlist.vue'),
    },
    {
      name: 'Adddepartment',
      path: '/adddepartment',
      component: () => import('@/pages/Departments/Adddepartment.vue'), 
    },
    {
      name: 'Servicesoffered',
      path: '/servicesoffered',
      component: () => import('@/pages/Departments/Servicesoffered.vue'),
    },
    {
      name: 'Inventorylist',
      path: '/inventorylist',
      component: () => import('@/pages/Inventory/Inventorylist.vue'),
    
    },
    {
      name: 'Additem',
      path: '/additem',
      component: () => import('@/pages/Inventory/Additem.vue'),
    },
    {
      name: 'Stockalerts',
      path: '/stockalerts',
      component: () => import('@/pages/Inventory/Stockalerts.vue'),
    },
    {
      name: 'Supplierslist',
      path: '/supplierslist',
      component: () => import('@/pages/Inventory/Supplierslist.vue'),
    }

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

<template>
	<div class="min-h-screen bg-gray-50 flex">
		<!-- Main Content -->
		<div class="flex-1 lg:ml-0">
			<!-- Dashboard Content -->
			<main class="p-6">
				<!-- Stats Cards -->
				<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
					<div
						v-for="stat in currentDashboard.stats"
						:key="stat.title"
						class="bg-white rounded-xl shadow-sm p-6 border hover:shadow-md transition-shadow duration-200"
					>
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm font-medium text-gray-600">{{ stat.title }}</p>
								<p class="text-2xl font-bold text-gray-900 mt-1">
									{{ stat.value }}
								</p>
								<p
									class="text-sm mt-1"
									:class="
										stat.change.includes('+')
											? 'text-green-600'
											: 'text-red-600'
									"
								>
									{{ stat.change }}
								</p>
							</div>
							<div class="p-3 rounded-lg" :class="stat.iconBg">
								<component
									:is="stat.icon"
									:class="stat.iconColor"
									class="w-6 h-6"
								/>
							</div>
						</div>
					</div>
				</div>

				<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
					<!-- Chart Section -->
					<div class="lg:col-span-2 bg-white rounded-xl shadow-sm p-6 border">
						<div class="flex items-center justify-between mb-6">
							<h3 class="text-lg font-semibold text-gray-900">Overview</h3>
							<div class="flex space-x-1 bg-gray-100 rounded-lg p-1">
								<button
									v-for="tab in chartTabs"
									:key="tab"
									@click="activeChartTab = tab"
									class="px-3 py-1 text-sm font-medium rounded-md transition-colors duration-200"
									:class="
										activeChartTab === tab
											? 'bg-white text-gray-900 shadow-sm'
											: 'text-gray-600 hover:text-gray-900'
									"
								>
									{{ tab }}
								</button>
							</div>
						</div>
						<p class="text-sm text-gray-600 mb-6">
							Patient visits and revenue for the current period.
						</p>

						<!-- Chart Placeholder -->
						<div
							class="h-64 bg-gray-50 rounded-lg flex items-end justify-center space-x-2 p-4"
						>
							<div
								v-for="(height, index) in chartData"
								:key="index"
								class="bg-blue-500 rounded-t transition-all duration-300 hover:bg-blue-600 relative group"
								:style="{ height: height + '%', width: '40px' }"
							>
								<div
									class="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-2 py-1 bg-gray-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 transition-opacity duration-200"
								>
									{{ Math.round(height * 50) }}
								</div>
							</div>
						</div>

						<div class="flex items-center justify-center mt-4 space-x-6">
							<div class="flex items-center space-x-2">
								<div class="w-3 h-3 bg-blue-500 rounded"></div>
								<span class="text-sm text-gray-600">Total</span>
							</div>
							<div class="flex items-center space-x-2">
								<div class="w-3 h-3 bg-green-500 rounded"></div>
								<span class="text-sm text-gray-600">Patients</span>
							</div>
						</div>
					</div>

					<!-- Recent Appointments -->
					<div class="bg-white rounded-xl shadow-sm p-6 border">
						<div class="flex items-center justify-between mb-6">
							<h3 class="text-lg font-semibold text-gray-900">
								Recent Appointments
							</h3>
							<button class="text-sm text-blue-600 hover:text-blue-700 font-medium">
								View all
							</button>
						</div>
						<p class="text-sm text-gray-600 mb-6">
							You have {{ currentDashboard.appointments.length }} appointments today.
						</p>

						<div class="space-y-4">
							<div
								v-for="appointment in currentDashboard.appointments"
								:key="appointment.id"
								class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 transition-colors duration-200"
							>
								<div
									class="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center"
								>
									<span class="text-sm font-medium text-gray-600">{{
										appointment.initials
									}}</span>
								</div>
								<div class="flex-1">
									<h4 class="text-sm font-medium text-gray-900">
										{{ appointment.name }}
									</h4>
									<p class="text-xs text-gray-500">{{ appointment.type }}</p>
									<p class="text-xs text-gray-400 flex items-center mt-1">
										<svg
											class="w-3 h-3 mr-1"
											fill="currentColor"
											viewBox="0 0 20 20"
										>
											<path
												fill-rule="evenodd"
												d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
												clip-rule="evenodd"
											/>
										</svg>
										Today @ {{ appointment.time }}
									</p>
								</div>
								<div>
									<span
										class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
										:class="
											appointment.status === 'Confirmed'
												? 'bg-green-100 text-green-800'
												: appointment.status === 'In Progress'
													? 'bg-yellow-100 text-yellow-800'
													: 'bg-blue-100 text-blue-800'
										"
									>
										{{ appointment.status }}
									</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</main>
		</div>

		<!-- Mobile Sidebar Overlay -->
		<div
			v-if="sidebarOpen"
			@click="sidebarOpen = false"
			class="fixed inset-0 bg-black bg-opacity-50 z-5 lg:hidden"
		></div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive state
const sidebarOpen = ref(false)
const activeDashboard = ref('admin')
const activeChartTab = ref('Overview')

// Dashboard configurations
const dashboards = [
	{
		id: 'admin',
		name: 'Admin Dashboard',
		icon: 'AdminIcon',
	},
	{
		id: 'doctor',
		name: 'Doctor Dashboard',
		icon: 'DoctorIcon',
	},
	{
		id: 'patient',
		name: 'Patient Dashboard',
		icon: 'PatientIcon',
	},
]

// Chart data and tabs
const chartTabs = ['Overview', 'Analytics', 'Reports', 'Notifications']
const chartData = [40, 60, 70, 75, 45, 85, 55, 35, 25, 65, 50, 35]

// Navigation items
const navigationItems = [
	{
		title: 'Management',
		items: [
			{ name: 'Doctors', icon: 'DoctorIcon', hasSubmenu: true },
			{ name: 'Patients', icon: 'PatientIcon', hasSubmenu: false },
			{ name: 'Appointments', icon: 'AppointmentIcon', hasSubmenu: true },
			{ name: 'Prescriptions', icon: 'PrescriptionIcon', hasSubmenu: true },
		],
	},
	{
		title: 'Services',
		items: [
			{ name: 'Ambulance', icon: 'AmbulanceIcon', hasSubmenu: true },
			{ name: 'Pharmacy', icon: 'PharmacyIcon', hasSubmenu: false },
			{ name: 'Blood Bank', icon: 'BloodBankIcon', hasSubmenu: true },
			{ name: 'Billing', icon: 'BillingIcon', hasSubmenu: true },
		],
	},
	{
		title: 'Operations',
		items: [
			{ name: 'Departments', icon: 'DepartmentIcon', hasSubmenu: false },
			{ name: 'Inventory', icon: 'InventoryIcon', hasSubmenu: true },
			{ name: 'Staff', icon: 'StaffIcon', hasSubmenu: true },
			{ name: 'Records', icon: 'RecordsIcon', hasSubmenu: true },
		],
	},
	{
		title: 'System',
		items: [
			{ name: 'Room Allotment', icon: 'RoomIcon', hasSubmenu: true },
			{ name: 'Reviews', icon: 'ReviewIcon', hasSubmenu: true },
			{ name: 'Feedback', icon: 'FeedbackIcon', hasSubmenu: false },
			{ name: 'Reports', icon: 'ReportIcon', hasSubmenu: false },
			{ name: 'Settings', icon: 'SettingsIcon', hasSubmenu: false },
		],
	},
]

// Dashboard data
const dashboardData = {
	admin: {
		title: 'Dashboard',
		subtitle: "Welcome back, Dr. Johnson! Here's what's happening today.",
		stats: [
			{
				title: 'Total Revenue',
				value: '$45,231.89',
				change: '+20.1% from last month',
				icon: 'RevenueIcon',
				iconBg: 'bg-green-100',
				iconColor: 'text-green-600',
			},
			{
				title: 'Appointments',
				value: '+2,350',
				change: '+10.1% from last month',
				icon: 'AppointmentIcon',
				iconBg: 'bg-blue-100',
				iconColor: 'text-blue-600',
			},
			{
				title: 'Patients',
				value: '+12,234',
				change: '+19% from last month',
				icon: 'PatientIcon',
				iconBg: 'bg-yellow-100',
				iconColor: 'text-yellow-600',
			},
			{
				title: 'Staff',
				value: '+573',
				change: '+4 new this month',
				icon: 'StaffIcon',
				iconBg: 'bg-purple-100',
				iconColor: 'text-purple-600',
			},
		],
		appointments: [
			{
				id: 1,
				name: 'John Smith',
				initials: 'JS',
				type: 'Check-up',
				time: '10:00 AM',
				status: 'Confirmed',
			},
			{
				id: 2,
				name: 'Emily Davis',
				initials: 'ED',
				type: 'Consultation',
				time: '11:30 AM',
				status: 'In Progress',
			},
			{
				id: 3,
				name: 'Robert Wilson',
				initials: 'RW',
				type: 'Follow-up',
				time: '09:15 AM',
				status: 'Completed',
			},
		],
	},
	doctor: {
		title: 'Doctor Dashboard',
		subtitle: 'Welcome back, Dr. Smith! Here are your patients today.',
		stats: [
			{
				title: "Today's Patients",
				value: '24',
				change: '+12% from yesterday',
				icon: 'PatientIcon',
				iconBg: 'bg-blue-100',
				iconColor: 'text-blue-600',
			},
			{
				title: 'Appointments',
				value: '18',
				change: '+5 pending',
				icon: 'AppointmentIcon',
				iconBg: 'bg-green-100',
				iconColor: 'text-green-600',
			},
			{
				title: 'Prescriptions',
				value: '156',
				change: '+8 this week',
				icon: 'PrescriptionIcon',
				iconBg: 'bg-yellow-100',
				iconColor: 'text-yellow-600',
			},
			{
				title: 'Consultations',
				value: '42',
				change: 'This week',
				icon: 'ConsultationIcon',
				iconBg: 'bg-purple-100',
				iconColor: 'text-purple-600',
			},
		],
		appointments: [
			{
				id: 1,
				name: 'Sarah Johnson',
				initials: 'SJ',
				type: 'Regular Checkup',
				time: '09:00 AM',
				status: 'Confirmed',
			},
			{
				id: 2,
				name: 'Mike Brown',
				initials: 'MB',
				type: 'Emergency',
				time: '10:30 AM',
				status: 'In Progress',
			},
			{
				id: 3,
				name: 'Lisa Anderson',
				initials: 'LA',
				type: 'Follow-up',
				time: '11:45 AM',
				status: 'Confirmed',
			},
		],
	},
	patient: {
		title: 'Patient Dashboard',
		subtitle: "Welcome back! Here's your health summary.",
		stats: [
			{
				title: 'Next Appointment',
				value: 'Tomorrow',
				change: '10:00 AM with Dr. Smith',
				icon: 'AppointmentIcon',
				iconBg: 'bg-blue-100',
				iconColor: 'text-blue-600',
			},
			{
				title: 'Prescriptions',
				value: '3 Active',
				change: '1 refill needed',
				icon: 'PrescriptionIcon',
				iconBg: 'bg-green-100',
				iconColor: 'text-green-600',
			},
			{
				title: 'Health Score',
				value: '85/100',
				change: '+5 this month',
				icon: 'HealthIcon',
				iconBg: 'bg-yellow-100',
				iconColor: 'text-yellow-600',
			},
			{
				title: 'Last Checkup',
				value: '2 weeks ago',
				change: 'All good',
				icon: 'CheckupIcon',
				iconBg: 'bg-purple-100',
				iconColor: 'text-purple-600',
			},
		],
		appointments: [
			{
				id: 1,
				name: 'Dr. Johnson',
				initials: 'DJ',
				type: 'Regular Checkup',
				time: '10:00 AM',
				status: 'Confirmed',
			},
			{
				id: 2,
				name: 'Dr. Williams',
				initials: 'DW',
				type: 'Specialist Consultation',
				time: '02:30 PM',
				status: 'Confirmed',
			},
			{
				id: 3,
				name: 'Dr. Davis',
				initials: 'DD',
				type: 'Lab Results',
				time: '04:00 PM',
				status: 'Pending',
			},
		],
	},
}

// Computed properties
const currentDashboard = computed(() => dashboardData[activeDashboard.value])
</script>

<!-- Icon Components -->
<script>
// Icon components as functional components
const AdminIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', { d: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' }),
	])

const DoctorIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z',
			clipRule: 'evenodd',
		}),
	])

const PatientIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z',
			clipRule: 'evenodd',
		}),
	])

const RevenueIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.305 2.305 0 01-.567-.267C8.07 8.34 8 8.114 8 8c0-.114.07-.34.433-.582zM11 12.849v-1.698c.22.071.412.164.567.267.364.243.433.468.433.582 0 .114-.07.34-.433.582a2.305 2.305 0 01-.567.267z',
		}),
	])

const AppointmentIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z',
			clipRule: 'evenodd',
		}),
	])

const StaffIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M13 6a3 3 0 11-6 0 3 3 0 016 0zM9 8a1 1 0 000 2v3a1 1 0 001 1h4a1 1 0 100-2v-3a1 1 0 000-2H9z',
		}),
	])

const PrescriptionIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z',
			clipRule: 'evenodd',
		}),
	])

const AmbulanceIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z',
			clipRule: 'evenodd',
		}),
	])

const PharmacyIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M10 18a8 8 0 100-16 8 8 0 000 16zM7 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 001-1V7a1 1 0 00-1-1H7a1 1 0 00-1 1v2z',
			clipRule: 'evenodd',
		}),
	])

const BloodBankIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z',
			clipRule: 'evenodd',
		}),
	])

const BillingIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zM14 6a2 2 0 012 2v8a2 2 0 01-2 2H6a2 2 0 01-2-2V8a2 2 0 012-2h8zM6 10a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h3a1 1 0 100-2H7z',
		}),
	])

const DepartmentIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-6a1 1 0 00-1-1H9a1 1 0 00-1 1v6a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z',
			clipRule: 'evenodd',
		}),
	])

const InventoryIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z',
		}),
	])

const RecordsIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z',
			clipRule: 'evenodd',
		}),
	])

const RoomIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z',
		}),
	])

const ReviewIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M10 2L13.09 8.26L20 9L15 13.74L16.18 20.5L10 17L3.82 20.5L5 13.74L0 9L6.91 8.26L10 2Z',
			clipRule: 'evenodd',
		}),
	])

const FeedbackIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z',
			clipRule: 'evenodd',
		}),
	])

const ReportIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			d: 'M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z',
		}),
	])

const SettingsIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z',
			clipRule: 'evenodd',
		}),
	])

const ConsultationIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M18 13V5a2 2 0 00-2-2H4a2 2 0 00-2 2v8a2 2 0 002 2h3l3 3 3-3h3a2 2 0 002-2zM5 7a1 1 0 011-1h8a1 1 0 110 2H6a1 1 0 01-1-1zm1 3a1 1 0 100 2h3a1 1 0 100-2H6z',
			clipRule: 'evenodd',
		}),
	])

const HealthIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z',
			clipRule: 'evenodd',
		}),
	])

const CheckupIcon = () =>
	h('svg', { class: 'w-5 h-5', fill: 'currentColor', viewBox: '0 0 20 20' }, [
		h('path', {
			fillRule: 'evenodd',
			d: 'M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z',
			clipRule: 'evenodd',
		}),
	])

// Export all components for global use
export {
	AdminIcon,
	DoctorIcon,
	PatientIcon,
	RevenueIcon,
	AppointmentIcon,
	StaffIcon,
	PrescriptionIcon,
	AmbulanceIcon,
	PharmacyIcon,
	BloodBankIcon,
	BillingIcon,
	DepartmentIcon,
	InventoryIcon,
	RecordsIcon,
	RoomIcon,
	ReviewIcon,
	FeedbackIcon,
	ReportIcon,
	SettingsIcon,
	ConsultationIcon,
	HealthIcon,
	CheckupIcon,
}
</script>

<style scoped>
/* Custom animations and transitions */
.slide-enter-active,
.slide-leave-active {
	transition: all 0.3s ease;
}

.slide-enter-from {
	transform: translateX(-100%);
}

.slide-leave-to {
	transform: translateX(-100%);
}

/* Custom scrollbar for sidebar */
.sidebar::-webkit-scrollbar {
	width: 4px;
}

.sidebar::-webkit-scrollbar-track {
	background: #f1f5f9;
}

.sidebar::-webkit-scrollbar-thumb {
	background: #cbd5e1;
	border-radius: 2px;
}

.sidebar::-webkit-scrollbar-thumb:hover {
	background: #94a3b8;
}

/* Chart animation */
.chart-bar {
	transition: all 0.3s ease;
	transform-origin: bottom;
}

.chart-bar:hover {
	transform: scaleY(1.05);
}

/* Loading animation for stats */
@keyframes pulse {
	0%,
	100% {
		opacity: 1;
	}
	50% {
		opacity: 0.8;
	}
}

.stat-card {
	animation: pulse 2s infinite;
}

/* Mobile responsiveness improvements */
@media (max-width: 768px) {
	.stats-grid {
		grid-template-columns: repeat(2, 1fr);
		gap: 1rem;
	}
}

@media (max-width: 640px) {
	.stats-grid {
		grid-template-columns: 1fr;
	}

	.chart-container {
		height: 200px;
	}
}

/* Dark mode support (optional) */
.dark .bg-white {
	background-color: #1f2937;
}

.dark .text-gray-900 {
	color: #f9fafb;
}

.dark .text-gray-600 {
	color: #d1d5db;
}

.dark .border {
	border-color: #374151;
}

/* Print styles */
@media print {
	.sidebar {
		display: none;
	}

	.main-content {
		margin-left: 0;
	}

	.no-print {
		display: none;
	}
}

/* Focus styles for accessibility */
button:focus,
a:focus {
	outline: 2px solid #3b82f6;
	outline-offset: 2px;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
	.bg-blue-50 {
		background-color: #dbeafe;
	}

	.text-blue-700 {
		color: #1d4ed8;
	}
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
	*,
	*::before,
	*::after {
		animation-duration: 0.01ms !important;
		animation-iteration-count: 1 !important;
		transition-duration: 0.01ms !important;
	}
}
</style>

<template>
	<div class="flex h-screen bg-gray-50">
		<!-- Overlay for mobile when sidebar is open -->
		<div
			v-if="!sidebarCollapsed"
			@click="toggleSidebar"
			class="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden"
		></div>

		<!-- Main Content -->
		<div
			:class="[
				'flex-1 flex flex-col overflow-hidden transition-all duration-300',
				'md:ml-0',
			]"
		>
			<!-- Dashboard Content -->
			<main class="flex-1 overflow-y-auto p-4 md:p-6">
				<!-- Stats Cards -->
				<div
					class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-6 md:mb-8"
				>
					<!-- Next Appointment -->
					<div
						class="bg-white rounded-lg shadow-sm p-4 md:p-6 border-l-4 border-blue-500"
					>
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Next Appointment</p>
								<p class="text-xl md:text-2xl font-bold text-gray-900">Tomorrow</p>
								<p class="text-xs text-gray-500">10:30 AM with Dr. Johnson</p>
								<button class="text-blue-600 text-sm hover:underline mt-2">
									View details >
								</button>
							</div>
							<svg
								class="w-6 h-6 md:w-8 md:h-8 text-blue-500"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path
									fill-rule="evenodd"
									d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
									clip-rule="evenodd"
								/>
							</svg>
						</div>
					</div>

					<!-- Medications -->
					<div
						class="bg-white rounded-lg shadow-sm p-4 md:p-6 border-l-4 border-green-500"
					>
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Medications</p>
								<p class="text-xl md:text-2xl font-bold text-gray-900">3 Active</p>
								<p class="text-xs text-gray-500">Next dose in 2 hours</p>
								<button class="text-green-600 text-sm hover:underline mt-2">
									View all medications >
								</button>
							</div>
							<svg
								class="w-6 h-6 md:w-8 md:h-8 text-green-500"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
							</svg>
						</div>
					</div>

					<!-- Test Results -->
					<div
						class="bg-white rounded-lg shadow-sm p-4 md:p-6 border-l-4 border-purple-500"
					>
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Test Results</p>
								<p class="text-xl md:text-2xl font-bold text-gray-900">2 New</p>
								<p class="text-xs text-gray-500">Blood work from 05/12</p>
								<button class="text-purple-600 text-sm hover:underline mt-2">
									View results >
								</button>
							</div>
							<svg
								class="w-6 h-6 md:w-8 md:h-8 text-purple-500"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path
									fill-rule="evenodd"
									d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
									clip-rule="evenodd"
								/>
							</svg>
						</div>
					</div>

					<!-- Billing -->
					<div
						class="bg-white rounded-lg shadow-sm p-4 md:p-6 border-l-4 border-red-500"
					>
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Billing</p>
								<p class="text-xl md:text-2xl font-bold text-gray-900">$45.00</p>
								<p class="text-xs text-gray-500">Due in 15 days</p>
								<button class="text-red-600 text-sm hover:underline mt-2">
									Make payment >
								</button>
							</div>
							<svg
								class="w-6 h-6 md:w-8 md:h-8 text-red-500"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path
									d="M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.305 2.305 0 01-.567-.267C8.07 8.34 8 8.114 8 8c0-.114.07-.34.433-.582zM11 12.849v-1.698c.22.071.412.164.567.267.364.243.433.468.433.582 0 .114-.07.34-.433.582a2.305 2.305 0 01-.567.267z"
								/>
								<path
									fill-rule="evenodd"
									d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-13a1 1 0 10-2 0v.092a4.535 4.535 0 00-1.676.662C6.602 6.234 6 7.009 6 8c0 .99.602 1.765 1.324 2.246.48.32 1.054.545 1.676.662v1.941c-.391-.127-.68-.317-.843-.504a1 1 0 10-1.51 1.31c.562.649 1.413 1.076 2.353 1.253V15a1 1 0 102 0v-.092a4.535 4.535 0 001.676-.662C13.398 13.766 14 12.991 14 12c0-.99-.602-1.765-1.324-2.246A4.535 4.535 0 0011 9.092V7.151c.391.127.68.317.843.504a1 1 0 101.511-1.31c-.563-.649-1.413-1.076-2.354-1.253V5z"
									clip-rule="evenodd"
								/>
							</svg>
						</div>
					</div>
				</div>

				<!-- Tab Navigation -->
				<div class="mb-6">
					<nav class="flex space-x-4 md:space-x-8 overflow-x-auto">
						<button
							v-for="tab in tabs"
							:key="tab.id"
							@click="activeTab = tab.id"
							:class="
								activeTab === tab.id
									? 'border-blue-500 text-blue-600'
									: 'border-transparent text-gray-500'
							"
							class="py-2 px-1 border-b-2 font-medium text-sm hover:text-gray-700 hover:border-gray-300 whitespace-nowrap"
						>
							{{ tab.label }}
						</button>
					</nav>
				</div>

				<!-- Main Content Grid -->
				<div class="grid grid-cols-1 lg:grid-cols-3 gap-4 md:gap-6">
					<!-- Health Summary -->
					<div class="lg:col-span-2 bg-white rounded-lg shadow-sm p-4 md:p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-2">Health Summary</h3>
						<p class="text-sm text-gray-600 mb-6">
							Your recent health metrics and goals
						</p>

						<div class="space-y-6">
							<!-- Health Metrics -->
							<div
								v-for="metric in healthMetrics"
								:key="metric.name"
								class="flex items-center justify-between"
							>
								<div class="flex items-center">
									<component
										:is="metric.icon"
										:class="metric.iconColor"
										class="w-6 h-6 mr-3"
									/>
									<div>
										<p class="font-medium text-gray-900">{{ metric.name }}</p>
										<p class="text-sm text-gray-600">{{ metric.range }}</p>
									</div>
								</div>
								<div class="text-right">
									<p class="text-lg md:text-xl font-bold text-gray-900">
										{{ metric.value }}
									</p>
									<div class="w-32 md:w-48 bg-gray-200 rounded-full h-2 mt-2">
										<div
											:class="metric.barColor"
											class="h-2 rounded-full"
											:style="`width: ${metric.percentage}%`"
										></div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<!-- Upcoming Appointments -->
					<div class="bg-white rounded-lg shadow-sm p-4 md:p-6">
						<div class="flex items-center justify-between mb-4">
							<h3 class="text-lg font-semibold text-gray-900">
								Upcoming Appointments
							</h3>
						</div>
						<p class="text-sm text-gray-600 mb-4">Your scheduled visits</p>

						<div class="space-y-4">
							<!-- Appointments -->
							<div
								v-for="appointment in appointments"
								:key="appointment.id"
								class="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg"
							>
								<div
									:class="appointment.avatarColor"
									class="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
								>
									<svg
										class="w-5 h-5 text-white"
										fill="currentColor"
										viewBox="0 0 20 20"
									>
										<path
											fill-rule="evenodd"
											d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
											clip-rule="evenodd"
										/>
									</svg>
								</div>
								<div class="flex-1 min-w-0">
									<div class="flex items-center justify-between">
										<p class="font-medium text-gray-900 truncate">
											{{ appointment.doctor }}
										</p>
										<span
											:class="appointment.badgeColor"
											class="text-xs px-2 py-1 rounded flex-shrink-0 ml-2"
											>{{ appointment.when }}</span
										>
									</div>
									<p class="text-sm text-gray-600">
										{{ appointment.specialty }}
									</p>
									<p class="text-xs text-gray-500">
										{{ appointment.date }} • {{ appointment.time }}
									</p>
									<p class="text-xs text-gray-500">{{ appointment.type }}</p>
								</div>
							</div>
						</div>

						<button class="w-full mt-4 text-blue-600 text-sm hover:underline">
							View All Appointments
						</button>
					</div>
				</div>

				<!-- Bottom Grid -->
				<div class="grid grid-cols-1 lg:grid-cols-3 gap-4 md:gap-6 mt-6">
					<!-- Medication Reminders -->
					<div class="bg-white rounded-lg shadow-sm p-4 md:p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">
							Medication Reminders
						</h3>
						<div class="space-y-3">
							<div
								class="flex items-center justify-between p-3 bg-blue-50 rounded-lg"
							>
								<div class="flex items-center min-w-0">
									<svg
										class="w-6 h-6 text-blue-600 mr-3 flex-shrink-0"
										fill="currentColor"
										viewBox="0 0 20 20"
									>
										<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
									</svg>
									<div class="min-w-0">
										<p class="font-medium text-gray-900">Metformin</p>
										<p class="text-sm text-gray-600">Take with breakfast</p>
									</div>
								</div>
								<span
									class="text-xs bg-blue-600 text-white px-2 py-1 rounded flex-shrink-0 ml-2"
									>Due Soon</span
								>
							</div>
						</div>
					</div>

					<!-- Recent Messages -->
					<div class="bg-white rounded-lg shadow-sm p-4 md:p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Recent Messages</h3>
						<div class="space-y-3">
							<div class="flex items-start space-x-3">
								<div
									class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center flex-shrink-0"
								>
									<svg
										class="w-4 h-4 text-gray-600"
										fill="currentColor"
										viewBox="0 0 20 20"
									>
										<path
											fill-rule="evenodd"
											d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
											clip-rule="evenodd"
										/>
									</svg>
								</div>
								<div class="min-w-0">
									<p class="text-sm font-medium text-gray-900">Dr. Johnson</p>
									<p class="text-xs text-gray-600">
										Your test results look good...
									</p>
									<p class="text-xs text-gray-400">2 hours ago</p>
								</div>
							</div>
						</div>
					</div>

					<!-- Health Tips -->
					<div class="bg-white rounded-lg shadow-sm p-4 md:p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Health Tips</h3>
						<div class="space-y-3">
							<div class="p-3 bg-green-50 rounded-lg">
								<p class="text-sm font-medium text-gray-900">Stay Hydrated</p>
								<p class="text-xs text-gray-600">
									Drink at least 8 glasses of water daily
								</p>
							</div>
						</div>
					</div>
				</div>
			</main>
		</div>
	</div>
</template>

<script setup>
// import { ref, inject } from 'vue'
// import { Dropdown } from 'frappe-ui'
// const session = inject('$session')

import { ref, inject, onMounted, onUnmounted } from 'vue'
import { Dropdown } from 'frappe-ui'
const session = inject('$session')

// Reactive state
const sidebarCollapsed = ref(false)
const expandedMenus = ref({
	dashboard: true,
})

const activeTab = ref('overview')

// Check if mobile on mount
onMounted(() => {
	const checkMobile = () => {
		sidebarCollapsed.value = window.innerWidth < 768
	}

	checkMobile()
	window.addEventListener('resize', checkMobile)

	onUnmounted(() => {
		window.removeEventListener('resize', checkMobile)
	})
})

// Reactive state
// const expandedMenus = ref({
// 	dashboard: true,
// })

// const activeTab = ref('overview')

// Menu items data
const menuItems = ref([
	// { name: 'doctors', label: 'Doctors', icon: 'UserIcon' },
	// { name: 'patients', label: 'Patients', icon: 'UsersIcon' },
	// { name: 'appointments', label: 'Appointments', icon: 'CalendarIcon' },
	// { name: 'prescriptions', label: 'Prescriptions', icon: 'ClipboardIcon' },
	// { name: 'ambulance', label: 'Ambulance', icon: 'TruckIcon' },
	// { name: 'pharmacy', label: 'Pharmacy', icon: 'BeakerIcon' },
	// { name: 'bloodbank', label: 'Blood Bank', icon: 'HeartIcon' },
	// { name: 'billing', label: 'Billing', icon: 'CurrencyDollarIcon' },
	// { name: 'departments', label: 'Departments', icon: 'BuildingOfficeIcon' },
	// { name: 'inventory', label: 'Inventory', icon: 'ArchiveBoxIcon' },
	// { name: 'staff', label: 'Staff', icon: 'UserGroupIcon' },
	// { name: 'records', label: 'Records', icon: 'FolderIcon' },
	// { name: 'room', label: 'Room Allotment', icon: 'HomeIcon' },
	// { name: 'reviews', label: 'Reviews', icon: 'StarIcon' },
	// { name: 'feedback', label: 'Feedback', icon: 'ChatBubbleLeftIcon' },
	// { name: 'reports', label: 'Reports', icon: 'ChartBarIcon' },
	// { name: 'settings', label: 'Settings', icon: 'CogIcon' },
])

// Tab navigation data
const tabs = ref([
	{ id: 'overview', label: 'Overview' },
	{ id: 'appointments', label: 'Appointments' },
	{ id: 'medications', label: 'Medications' },
	{ id: 'records', label: 'Records' },
	{ id: 'vitals', label: 'Vitals' },
])

// Health metrics data
const healthMetrics = ref([
	{
		name: 'Heart Rate',
		range: 'Normal range: 60-100 BPM',
		value: '72 BPM',
		percentage: 65,
		icon: 'HeartIcon',
		iconColor: 'text-red-500',
		barColor: 'bg-green-500',
	},
	{
		name: 'Blood Pressure',
		range: 'Normal range: Below 120/80 mmHg',
		value: '118/78 mmHg',
		percentage: 70,
		icon: 'ActivityIcon',
		iconColor: 'text-blue-500',
		barColor: 'bg-green-500',
	},
	{
		name: 'Glucose Level',
		range: 'Normal range: 70-140 mg/dL',
		value: '98 mg/dL',
		percentage: 60,
		icon: 'ExclamationTriangleIcon',
		iconColor: 'text-yellow-500',
		barColor: 'bg-green-500',
	},
])

// Appointments data
const appointments = ref([
	{
		id: 1,
		doctor: 'Dr. Johnson',
		specialty: 'Cardiology',
		date: 'May 15, 2023',
		time: '10:30 AM',
		type: 'Annual checkup',
		when: 'Tomorrow',
		avatarColor: 'bg-blue-100',
		badgeColor: 'bg-blue-100 text-blue-800',
	},
	{
		id: 2,
		doctor: 'Dr. Martinez',
		specialty: 'Dermatology',
		date: 'May 22, 2023',
		time: '2:15 PM',
		type: 'Skin examination',
		when: 'Next Week',
		avatarColor: 'bg-green-100',
		badgeColor: 'bg-green-100 text-green-800',
	},
])

// Methods
const toggleMenu = (menu) => {
	expandedMenus.value[menu] = !expandedMenus.value[menu]
}
// Add this method if it doesn't exist
const toggleSidebar = () => {
	sidebarCollapsed.value = !sidebarCollapsed.value
}
// SVG Icon Components
const HeartIcon = {
	template: `<svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" /></svg>`,
}

const ActivityIcon = {
	template: `<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" /></svg>`,
}

const ExclamationTriangleIcon = {
	template: `<svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>`,
}

const UserIcon = {
	template: `<svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" /></svg>`,
}
</script>

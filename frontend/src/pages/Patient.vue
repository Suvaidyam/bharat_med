<template>
	<div class="flex h-screen bg-gray-50">
		<!-- Sidebar -->
		<div class="w-64 bg-white shadow-lg">
			<!-- Logo -->
			<div class="flex items-center px-6 py-4 border-b">
				<div class="flex items-center">
					<!-- <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
						<svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
							<path
								fill-rule="evenodd"
								d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"
								clip-rule="evenodd"
							/>
						</svg>
					</div> -->
					<span class="ml-3 text-xl font-semibold text-gray-800">Suvaidyam</span>
				</div>
			</div>

			<!-- Navigation -->
			<nav class="mt-6 px-4">
				<!-- Dashboard Section -->
				<div class="mb-2">
					<button
						@click="toggleMenu('dashboard')"
						class="w-full flex items-center justify-between px-2 py-2 text-gray-600 hover:bg-gray-100 rounded-lg"
					>
						<div class="flex items-center">
							<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
								<path
									d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"
								/>
							</svg>
							<span class="ml-3 text-sm">Dashboard</span>
						</div>
						<svg
							:class="expandedMenus.dashboard ? 'rotate-90' : ''"
							class="w-4 h-4 transform transition-transform"
							fill="currentColor"
							viewBox="0 0 20 20"
						>
							<path
								fill-rule="evenodd"
								d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
								clip-rule="evenodd"
							/>
						</svg>
					</button>
					<div v-show="expandedMenus.dashboard" class="ml-6 mt-2 space-y-1">
						<!-- <a
							href="#"
							class="block px-3 py-2 text-sm text-blue-600 bg-blue-50 rounded-lg"
							>Admin Dashboard</a
						> -->
						<!-- <a
							href="#"
							class="block px-3 py-2 text-sm text-gray-600 hover:bg-gray-100 rounded-lg"
							>Doctor Dashboard</a
						> -->
						<a
							href="#"
							class="block px-3 py-2 text-sm text-gray-600 hover:bg-gray-100 rounded-lg"
							>Patient Dashboard</a
						>
					</div>
				</div>

				<!-- Other Menu Items -->
				<div class="space-y-1">
					<button
						v-for="item in menuItems"
						:key="item.name"
						@click="toggleMenu(item.name)"
						class="w-full flex items-center justify-between px-2 py-2 text-gray-600 hover:bg-gray-100 rounded-lg"
					>
						<div class="flex items-center">
							<component :is="item.icon" class="w-5 h-5" />
							<span class="ml-3 text-sm">{{ item.label }}</span>
						</div>
						<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
							<path
								fill-rule="evenodd"
								d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
								clip-rule="evenodd"
							/>
						</svg>
					</button>
				</div>
			</nav>
		</div>

		<!-- Main Content -->
		<div class="flex-1 flex flex-col overflow-hidden">
			<!-- Top Header -->
			<header class="bg-white shadow-sm border-b px-6 py-4">
				<div class="flex items-center justify-between">
					<div>
						<h1 class="text-2xl font-bold text-gray-900">Welcome back, Vrindarak</h1>
						<p class="text-gray-600 text-sm">
							Your health dashboard - manage your care all in one place
						</p>
					</div>
					<div class="flex items-center space-x-4">
						<button
							class="flex items-center px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50"
						>
							<svg
								class="w-4 h-4 mr-2 text-blue-600"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path
									fill-rule="evenodd"
									d="M18 13V5a2 2 0 00-2-2H4a2 2 0 00-2 2v8a2 2 0 002 2h3l3 3 3-3h3a2 2 0 002-2zM5 7a1 1 0 011-1h8a1 1 0 110 2H6a1 1 0 01-1-1zm1 3a1 1 0 100 2h3a1 1 0 100-2H6z"
									clip-rule="evenodd"
								/>
							</svg>
							<span class="text-sm text-gray-700">Message Doctor</span>
						</button>
						<button
							class="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
						>
							<svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
								<path
									fill-rule="evenodd"
									d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
									clip-rule="evenodd"
								/>
							</svg>
							<span class="text-sm">Book Appointment</span>
						</button>
						<div class="flex items-center space-x-2">
							<svg
								class="w-5 h-5 text-gray-400"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path
									d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"
								/>
							</svg>
							<span
								class="text-sm font-medium text-gray-700 w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center"
								>V</span
							>
						</div>
					</div>
				</div>
			</header>

			<!-- Dashboard Content -->
			<main class="flex-1 overflow-y-auto p-6">
				<!-- Stats Cards -->
				<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
					<!-- Next Appointment -->
					<div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-blue-500">
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Next Appointment</p>
								<p class="text-2xl font-bold text-gray-900">Tomorrow</p>
								<p class="text-xs text-gray-500">10:30 AM with Dr. Johnson</p>
								<button class="text-blue-600 text-sm hover:underline mt-2">
									View details >
								</button>
							</div>
							<svg
								class="w-8 h-8 text-blue-500"
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
					<div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-green-500">
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Medications</p>
								<p class="text-2xl font-bold text-gray-900">3 Active</p>
								<p class="text-xs text-gray-500">Next dose in 2 hours</p>
								<button class="text-green-600 text-sm hover:underline mt-2">
									View all medications >
								</button>
							</div>
							<svg
								class="w-8 h-8 text-green-500"
								fill="currentColor"
								viewBox="0 0 20 20"
							>
								<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
							</svg>
						</div>
					</div>

					<!-- Test Results -->
					<div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-purple-500">
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Test Results</p>
								<p class="text-2xl font-bold text-gray-900">2 New</p>
								<p class="text-xs text-gray-500">Blood work from 05/12</p>
								<button class="text-purple-600 text-sm hover:underline mt-2">
									View results >
								</button>
							</div>
							<svg
								class="w-8 h-8 text-purple-500"
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
					<div class="bg-white rounded-lg shadow-sm p-6 border-l-4 border-red-500">
						<div class="flex items-center justify-between">
							<div>
								<p class="text-sm text-gray-600 mb-1">Billing</p>
								<p class="text-2xl font-bold text-gray-900">$45.00</p>
								<p class="text-xs text-gray-500">Due in 15 days</p>
								<button class="text-red-600 text-sm hover:underline mt-2">
									Make payment >
								</button>
							</div>
							<svg
								class="w-8 h-8 text-red-500"
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
					<nav class="flex space-x-8">
						<button
							v-for="tab in tabs"
							:key="tab.id"
							@click="activeTab = tab.id"
							:class="
								activeTab === tab.id
									? 'border-blue-500 text-blue-600'
									: 'border-transparent text-gray-500'
							"
							class="py-2 px-1 border-b-2 font-medium text-sm hover:text-gray-700 hover:border-gray-300"
						>
							{{ tab.label }}
						</button>
					</nav>
				</div>

				<!-- Main Content Grid -->
				<div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
					<!-- Health Summary -->
					<div class="lg:col-span-2 bg-white rounded-lg shadow-sm p-6">
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
									<p class="text-xl font-bold text-gray-900">
										{{ metric.value }}
									</p>
									<div class="w-48 bg-gray-200 rounded-full h-2 mt-2">
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
					<div class="bg-white rounded-lg shadow-sm p-6">
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
									class="w-10 h-10 rounded-full flex items-center justify-center"
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
								<div class="flex-1">
									<div class="flex items-center justify-between">
										<p class="font-medium text-gray-900">
											{{ appointment.doctor }}
										</p>
										<span
											:class="appointment.badgeColor"
											class="text-xs px-2 py-1 rounded"
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
				<div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
					<!-- Medication Reminders -->
					<div class="bg-white rounded-lg shadow-sm p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">
							Medication Reminders
						</h3>
						<div class="space-y-3">
							<div
								class="flex items-center justify-between p-3 bg-blue-50 rounded-lg"
							>
								<div class="flex items-center">
									<svg
										class="w-6 h-6 text-blue-600 mr-3"
										fill="currentColor"
										viewBox="0 0 20 20"
									>
										<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
									</svg>
									<div>
										<p class="font-medium text-gray-900">Metformin</p>
										<p class="text-sm text-gray-600">Take with breakfast</p>
									</div>
								</div>
								<span class="text-xs bg-blue-600 text-white px-2 py-1 rounded"
									>Due Soon</span
								>
							</div>
						</div>
					</div>

					<!-- Recent Messages -->
					<div class="bg-white rounded-lg shadow-sm p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Recent Messages</h3>
						<div class="space-y-3">
							<div class="flex items-start space-x-3">
								<div
									class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center"
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
								<div>
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
					<div class="bg-white rounded-lg shadow-sm p-6">
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
import { ref } from 'vue'

// Reactive state
const expandedMenus = ref({
	dashboard: true,
})

const activeTab = ref('overview')

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

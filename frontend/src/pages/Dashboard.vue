<template>
	<div class="flex h-screen bg-gray-50 font-sans">
		<!-- Sidebar -->
		<div
			:class="[
				sidebarExpanded ? 'w-64' : 'w-16',
				'transition-all duration-300 bg-white shadow-sm border-r border-gray-200 flex flex-col',
			]"
		>
			<!-- Logo -->
			<div class="p-4 border-b border-gray-200">
				<div class="flex items-center">
					<!-- <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
						<PlusIcon class="w-5 h-5 text-white" />
					</div> -->
					<span v-if="sidebarExpanded" class="ml-3 text-lg font-semibold text-gray-900"
						>Suvaidyam</span
					>
				</div>
			</div>

			<!-- Navigation -->
			<div class="flex-1 overflow-y-auto py-4">
				<div
					v-for="(item, index) in sidebarItems"
					:key="index"
					:class="['px-3 py-1', item.active ? 'bg-blue-50' : '']"
				>
					<div
						:class="[
							'flex items-center px-3 py-2 text-sm rounded-lg cursor-pointer hover:bg-gray-50',
							item.active ? 'text-blue-700 bg-blue-50' : 'text-gray-700',
						]"
					>
						<component :is="item.icon" class="w-5 h-5" />
						<template v-if="sidebarExpanded">
							<span class="ml-3 flex-1">{{ item.label }}</span>
							<ChevronDownIcon v-if="item.hasSubmenu" class="w-4 h-4" />
						</template>
					</div>
					<!-- Submenu for Dashboard -->
					<div v-if="item.active && sidebarExpanded" class="ml-8 mt-1 space-y-1">
						<!-- <div class="px-3 py-1 text-sm text-blue-600 cursor-pointer">
							Admin Dashboard
						</div> -->
						<div class="px-3 py-1 text-sm text-blue-600 cursor-pointer font-medium">
							Doctor Dashboard
						</div>
						<div class="px-3 py-1 text-sm text-gray-600 cursor-pointer">
							Patient Dashboard
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Main Content -->
		<div class="flex-1 flex flex-col overflow-hidden">
			<!-- Header -->
			<header class="bg-white border-b border-gray-200 px-6 py-4">
				<div class="flex items-center justify-between">
					<div>
						<h1 class="text-2xl font-semibold text-gray-900">
							Welcome back, Dr. Vrindarak
						</h1>
						<p class="text-gray-600 mt-1">
							Here's what's happening with your patients today.
						</p>
					</div>
					<div class="flex items-center space-x-4">
						<SearchIcon class="w-5 h-5 text-gray-400" />
						<div class="relative">
							<BellIcon class="w-5 h-5 text-gray-400" />
							<div
								class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"
							></div>
						</div>
						<div class="flex items-center space-x-2">
							<div
								class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center"
							>
								<span class="text-white text-sm font-medium">V</span>
							</div>
						</div>
					</div>
				</div>
			</header>

			<!-- Dashboard Cards -->
			<div class="p-6 overflow-y-auto">
				<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
					<!-- Appointments Card -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<div
									class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center"
								>
									<CalendarIcon class="w-5 h-5 text-blue-600" />
								</div>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">Appointments</p>
									<p class="text-xs text-red-600">3 urgent</p>
								</div>
							</div>
						</div>
						<div class="mb-4">
							<div class="text-3xl font-bold text-gray-900">12</div>
							<p class="text-sm text-gray-600">Today's consultations</p>
						</div>
						<button
							class="text-blue-600 text-sm font-medium hover:text-blue-700 flex items-center"
						>
							View Schedule <ChevronRightIcon class="w-4 h-4 ml-1" />
						</button>
					</div>

					<!-- Pending Reports Card -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<div
									class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center"
								>
									<FileTextIcon class="w-5 h-5 text-green-600" />
								</div>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">
										Pending Reports
									</p>
									<p class="text-xs text-green-600">2 ready</p>
								</div>
							</div>
						</div>
						<div class="mb-4">
							<div class="text-3xl font-bold text-gray-900">7</div>
							<p class="text-sm text-gray-600">Lab results awaiting review</p>
						</div>
						<button
							class="text-green-600 text-sm font-medium hover:text-green-700 flex items-center"
						>
							Review Reports <ChevronRightIcon class="w-4 h-4 ml-1" />
						</button>
					</div>

					<!-- Active Patients Card -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<div
									class="w-10 h-10 bg-yellow-100 rounded-lg flex items-center justify-center"
								>
									<UsersIcon class="w-5 h-5 text-yellow-600" />
								</div>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">
										Active Patients
									</p>
									<p class="text-xs text-yellow-600">8 new</p>
								</div>
							</div>
						</div>
						<div class="mb-4">
							<div class="text-3xl font-bold text-gray-900">143</div>
							<p class="text-sm text-gray-600">Total patient count this week</p>
						</div>
						<button
							class="text-yellow-600 text-sm font-medium hover:text-yellow-700 flex items-center"
						>
							Patient Records <ChevronRightIcon class="w-4 h-4 ml-1" />
						</button>
					</div>

					<!-- Pending Tasks Card -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
						<div class="flex items-center justify-between mb-4">
							<div class="flex items-center">
								<div
									class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center"
								>
									<CheckSquareIcon class="w-5 h-5 text-red-600" />
								</div>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">Pending Tasks</p>
									<p class="text-xs text-red-600">2 high priority</p>
								</div>
							</div>
						</div>
						<div class="mb-4">
							<div class="text-3xl font-bold text-gray-900">5</div>
							<p class="text-sm text-gray-600">Tasks requiring attention</p>
						</div>
						<button
							class="text-red-600 text-sm font-medium hover:text-red-700 flex items-center"
						>
							View Tasks <ChevronRightIcon class="w-4 h-4 ml-1" />
						</button>
					</div>
				</div>

				<!-- Tabs -->
				<div class="border-b border-gray-200 mb-6">
					<nav class="-mb-px flex space-x-8">
						<button
							v-for="tab in tabs"
							:key="tab"
							@click="activeTab = tab"
							:class="[
								'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm',
								activeTab === tab
									? 'border-blue-500 text-blue-600'
									: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
							]"
						>
							{{ tab }}
						</button>
					</nav>
				</div>

				<!-- Content Grid -->
				<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
					<!-- Today's Schedule -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200">
						<div class="p-6 border-b border-gray-200">
							<h3 class="text-lg font-semibold text-gray-900">Today's Schedule</h3>
							<p class="text-sm text-gray-600 mt-1">
								You have 12 appointments scheduled for today
							</p>
						</div>
						<div class="p-6 space-y-4">
							<div
								v-for="(appointment, index) in todayAppointments"
								:key="index"
								class="flex items-center justify-between p-4 hover:bg-gray-50 rounded-lg"
							>
								<div class="flex items-center space-x-4">
									<div
										class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center"
									>
										<span class="text-white text-sm font-medium">{{
											appointment.avatar
										}}</span>
									</div>
									<div>
										<h4 class="font-medium text-gray-900">
											{{ appointment.name }}
										</h4>
										<div
											class="flex items-center text-sm text-gray-600 space-x-2"
										>
											<ClockIcon class="w-4 h-4" />
											<span>{{ appointment.time }}</span>
											<span v-if="appointment.duration"
												>• {{ appointment.duration }}</span
											>
										</div>
									</div>
								</div>
								<div class="flex items-center space-x-3">
									<span
										:class="[
											'px-2 py-1 rounded-full text-xs font-medium',
											getStatusBadgeClass(appointment.status),
										]"
									>
										{{ getStatusText(appointment.status) }}
									</span>
									<button
										class="text-blue-600 hover:text-blue-700 text-sm font-medium"
									>
										View
									</button>
								</div>
							</div>
						</div>
					</div>

					<!-- Upcoming Appointments -->
					<div class="bg-white rounded-lg shadow-sm border border-gray-200">
						<div class="p-6 border-b border-gray-200">
							<h3 class="text-lg font-semibual text-gray-900">
								Upcoming Appointments
							</h3>
							<p class="text-sm text-gray-600 mt-1">
								Your upcoming appointments for the week
							</p>
						</div>
						<div class="p-6 space-y-4">
							<div
								v-for="(appointment, index) in upcomingAppointments"
								:key="index"
								class="flex items-center justify-between p-4 hover:bg-gray-50 rounded-lg"
							>
								<div>
									<h4 class="font-medium text-gray-900">
										{{ appointment.name }}
									</h4>
									<p class="text-sm text-gray-600">{{ appointment.date }}</p>
								</div>
								<div class="flex items-center space-x-3">
									<span
										:class="[
											'px-2 py-1 rounded-full text-xs font-medium',
											getStatusBadgeClass(appointment.status),
										]"
									>
										{{ getStatusText(appointment.status) }}
									</span>
									<span
										:class="[
											'px-2 py-1 rounded text-xs font-medium',
											getTypeClass(appointment.type),
										]"
									>
										{{ appointment.type }}
									</span>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import {
	PlusIcon,
	ChevronDownIcon,
	ChevronRightIcon,
	SearchIcon,
	BellIcon,
	CalendarIcon,
	FileTextIcon,
	UsersIcon,
	CheckSquareIcon,
	ClockIcon,
	BarChart3Icon,
	UserCheckIcon,
	ActivityIcon,
	PillIcon,
	BuildingIcon,
	ClipboardListIcon,
	FolderIcon,
	StarIcon,
	SettingsIcon,
} from 'lucide-vue-next'

// Reactive state
const sidebarExpanded = ref(true)
const activeTab = ref('Schedule')

// Static data
const tabs = ['Schedule', 'Patients', 'Tasks', 'Stats']

const sidebarItems = [
	{ icon: BarChart3Icon, label: 'Dashboard', hasSubmenu: true, active: true },
	// { icon: UserCheckIcon, label: 'Doctors', hasSubmenu: true },
	// { icon: UsersIcon, label: 'Patients' },
	// { icon: CalendarIcon, label: 'Appointments', hasSubmenu: true },
	// { icon: PillIcon, label: 'Prescriptions', hasSubmenu: true },
	// { icon: ActivityIcon, label: 'Ambulance', hasSubmenu: true },
	// { icon: PillIcon, label: 'Pharmacy', hasSubmenu: true },
	// { icon: BuildingIcon, label: 'Blood Bank', hasSubmenu: true },
	// { icon: ClipboardListIcon, label: 'Billing', hasSubmenu: true },
	// { icon: BuildingIcon, label: 'Departments', hasSubmenu: true },
	// { icon: FolderIcon, label: 'Inventory', hasSubmenu: true },
	// { icon: UsersIcon, label: 'Staff', hasSubmenu: true },
	// { icon: FileTextIcon, label: 'Records', hasSubmenu: true },
	// { icon: CalendarIcon, label: 'Room Allotment', hasSubmenu: true },
	// { icon: StarIcon, label: 'Reviews', hasSubmenu: true },
	// { icon: FileTextIcon, label: 'Feedback' },
	// { icon: BarChart3Icon, label: 'Reports', hasSubmenu: true },
	// { icon: SettingsIcon, label: 'Settings', hasSubmenu: true },
]

const todayAppointments = [
	{
		name: 'Emma Thompson',
		time: '09:00 AM',
		duration: '30 min',
		type: 'Check-up',
		status: 'check-up',
		avatar: 'ET',
	},
	{
		name: 'Michael Chen',
		time: '10:15 AM',
		duration: '45 min',
		type: 'Follow-up',
		status: 'follow-up',
		avatar: 'MC',
	},
	{
		name: 'Sophia Rodriguez',
		time: '11:30 AM',
		duration: '60 min',
		type: 'Consultation',
		status: 'consultation',
		avatar: 'SR',
	},
	{
		name: 'James Wilson',
		time: '01:45 PM',
		duration: '30 min',
		type: 'Urgent',
		status: 'urgent',
		avatar: 'JW',
	},
	{
		name: 'Olivia Parker',
		time: '',
		duration: '',
		type: 'Check-up',
		status: 'check-up',
		avatar: 'OP',
	},
]

const upcomingAppointments = [
	{
		name: 'John Doe',
		date: 'Saturday, April 26 at 09:00 AM',
		type: 'Follow-up',
		status: 'confirmed',
	},
	{
		name: 'Jane Smith',
		date: 'Saturday, April 26 at 10:30 AM',
		type: 'New Patient',
		status: 'pending',
	},
	{
		name: 'Robert Johnson',
		date: 'Sunday, April 27 at 02:00 PM',
		type: 'Consultation',
		status: 'confirmed',
	},
	{
		name: 'Emily Davis',
		date: 'Monday, April 28 at 11:00 AM',
		type: 'Follow-up',
		status: 'confirmed',
	},
	{
		name: 'John Doe',
		date: 'Tuesday, April 29 at 09:00 AM',
		type: 'New Patient',
		status: 'pending',
	},
]

// Utility functions
const getStatusBadgeClass = (status) => {
	switch (status) {
		case 'check-up':
			return 'bg-blue-100 text-blue-800 border border-blue-200'
		case 'follow-up':
			return 'bg-gray-100 text-gray-800 border border-gray-200'
		case 'consultation':
			return 'bg-purple-100 text-purple-800 border border-purple-200'
		case 'urgent':
			return 'bg-red-100 text-red-800 border border-red-200'
		case 'confirmed':
			return 'bg-green-100 text-green-800 border border-green-200'
		case 'pending':
			return 'bg-yellow-100 text-yellow-800 border border-yellow-200'
		default:
			return 'bg-gray-100 text-gray-800 border border-gray-200'
	}
}

const getStatusText = (status) => {
	switch (status) {
		case 'check-up':
			return 'Check-up'
		case 'follow-up':
			return 'Follow-up'
		case 'consultation':
			return 'Consultation'
		case 'urgent':
			return 'Urgent'
		case 'confirmed':
			return 'confirmed'
		case 'pending':
			return 'pending'
		default:
			return status
	}
}

const getTypeClass = (type) => {
	switch (type) {
		case 'New Patient':
			return 'bg-yellow-100 text-yellow-800'
		case 'Follow-up':
			return 'bg-blue-100 text-blue-800'
		default:
			return 'bg-purple-100 text-purple-800'
	}
}
</script>

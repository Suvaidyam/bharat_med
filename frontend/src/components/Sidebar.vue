<!-- components/Sidebar.vue -->
<template>
	<div
		:class="[
			expanded ? 'w-64' : 'w-16 md:w-16 w-12',
			'transition-all duration-300 bg-white shadow-sm border-r border-gray-200 flex flex-col',
		]"
	>
		<!-- Logo -->
		<div class="p-4 border-b border-gray-200">
			<div class="flex items-center">
				<span
					v-if="expanded"
					class="ml-3 text-lg font-semibold text-gray-900 cursor-pointer hover:text-blue-600 transition-colors"
					@click="toggleSidebar"
				>
					Suvaidyam
				</span>
				<!-- Hamburger icon for collapsed state -->
				<button
					v-else
					@click="toggleSidebar"
					class="w-8 h-8 flex items-center justify-center hover:bg-gray-100 rounded-lg transition-colors"
				>
					<svg
						class="w-5 h-5 text-gray-600"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h16M4 18h16"
						></path>
					</svg>
				</button>
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
					@click="handleItemClick(item)"
				>
					<component :is="item.icon" class="w-5 h-5" />
					<template v-if="expanded">
						<span class="ml-3 flex-1">{{ item.label }}</span>
						<ChevronDownIcon
							v-if="item.hasSubmenu"
							:class="[
								'w-4 h-4 transition-transform',
								item.active ? 'rotate-180' : '',
							]"
						/>
					</template>
				</div>

				<!-- Submenu -->
				<div
					v-if="item.active && expanded && item.hasSubmenu && item.submenu"
					class="ml-8 mt-1 space-y-1"
				>
					<div
						v-for="submenu in item.submenu"
						:key="submenu.label"
						:class="[
							'px-3 py-1 text-sm cursor-pointer rounded hover:bg-blue-50 transition-colors',
							submenu.active
								? 'text-blue-600 font-medium bg-blue-50'
								: 'text-gray-600 hover:text-blue-600',
						]"
						@click.stop="handleSubmenuClick(item, submenu)"
					>
						{{ submenu.label }}
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
	ChevronDownIcon,
	BarChart3Icon,
	UserCheckIcon,
	UsersIcon,
	CalendarIcon,
	PillIcon,
	ActivityIcon,
	BuildingIcon,
	ClipboardListIcon,
	FolderIcon,
	StarIcon,
	SettingsIcon,
	FileTextIcon,
} from 'lucide-vue-next'

// Router

// Props

// Emits

// Data
const sidebarItems = ref([
	{
		icon: BarChart3Icon,
		label: 'Dashboard',
		hasSubmenu: true,
		active: false,
		route: '/dashboard',
		submenu: [
			{ label: 'Admin Dashboard', active: true, route: '/dashboard/admindash' },
			{
				label: 'Doctor Dashboard',
				active: false,
				route: '/dashboard/doctordash',
			},
			{
				label: 'Patient Dashboard',
				active: false,
				route: '/dashboard/patient',
			},
		],
	},
	{
		icon: UserCheckIcon,
		label: 'Doctors',
		hasSubmenu: true,
		active: false,
		route: '/dashboard',
		submenu: [
			{ label: 'Doctors List', active: false, route: '/doctorlist' },
			{ label: 'Add Doctor', active: false, route: '/adddoctor' },
			{ label: 'Doctor Schedule', active: false, route: '/doctorschedule' },
			{ label: 'Specializations', active: false, route: '/specializations' },
		],
	},
	{ icon: UsersIcon, label: 'Patients', route: '/addpatientviewlist' },
	{
		icon: CalendarIcon,
		label: 'Appointments',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'All Appointments', active: false, route: '/appointments/all' },
			{
				label: "Today's Appointments",
				active: false,
				route: '/appointments/today',
			},
			{
				label: 'Schedule Appointment',
				active: false,
				route: '/appointments/schedule',
			},
		],
	},
	{
		icon: PillIcon,
		label: 'Prescriptions',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'All Prescriptions',
				active: false,
				route: '/prescriptions/all',
			},
			{
				label: 'Create Prescription',
				active: false,
				route: '/prescriptions/create',
			},
		],
	},
	{
		icon: ActivityIcon,
		label: 'Ambulance',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'Available Ambulances',
				active: false,
				route: '/ambulance/available',
			},
			{ label: 'Book Ambulance', active: false, route: '/ambulance/book' },
		],
	},
	{
		icon: PillIcon,
		label: 'Pharmacy',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'Medicine Inventory',
				active: false,
				route: '/pharmacy/inventory',
			},
			{ label: 'Orders', active: false, route: '/pharmacy/orders' },
		],
	},
	{
		icon: BuildingIcon,
		label: 'Blood Bank',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'Blood Inventory',
				active: false,
				route: '/blood-bank/inventory',
			},
			{ label: 'Donors', active: false, route: '/blood-bank/donors' },
		],
	},
	{
		icon: ClipboardListIcon,
		label: 'Billing',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'All Bills', active: false, route: '/billing/all' },
			{ label: 'Generate Bill', active: false, route: '/billing/generate' },
		],
	},
	{
		icon: BuildingIcon,
		label: 'Departments',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'All Departments', active: false, route: '/departments/all' },
			{ label: 'Add Department', active: false, route: '/departments/add' },
		],
	},
	{
		icon: FolderIcon,
		label: 'Inventory',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'Medical Equipment',
				active: false,
				route: '/inventory/equipment',
			},
			{ label: 'Supplies', active: false, route: '/inventory/supplies' },
		],
	},
	{
		icon: UsersIcon,
		label: 'Staff',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'All Staff', active: false, route: '/staff/all' },
			{ label: 'Add Staff', active: false, route: '/staff/add' },
		],
	},
	{
		icon: FileTextIcon,
		label: 'Records',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'Patient Records', active: false, route: '/records/patients' },
			{ label: 'Medical History', active: false, route: '/records/history' },
		],
	},
	{
		icon: CalendarIcon,
		label: 'Room Allotment',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'Available Rooms', active: false, route: '/rooms/available' },
			{ label: 'Room Bookings', active: false, route: '/rooms/bookings' },
		],
	},
	{
		icon: StarIcon,
		label: 'Reviews',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'Patient Reviews', active: false, route: '/reviews/patients' },
			{ label: 'Doctor Reviews', active: false, route: '/reviews/doctors' },
		],
	},
	{ icon: FileTextIcon, label: 'Feedback', route: '/feedback' },
	{
		icon: BarChart3Icon,
		label: 'Reports',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{
				label: 'Financial Reports',
				active: false,
				route: '/reports/financial',
			},
			{ label: 'Patient Reports', active: false, route: '/reports/patients' },
		],
	},
	{
		icon: SettingsIcon,
		label: 'Settings',
		hasSubmenu: true,
		route: '/dashboard',
		submenu: [
			{ label: 'General Settings', active: false, route: '/settings/general' },
			{ label: 'User Management', active: false, route: '/settings/users' },
		],
	},
])

// Methods

// ... icon imports remain unchanged ...

// Router
const router = useRouter()
const route = useRoute()

// Props
const props = defineProps({
	expanded: {
		type: Boolean,
		default: true,
	},
})

// Emits
const emit = defineEmits(['toggle-sidebar', 'navigate'])

// Methods
const toggleSidebar = () => {
	emit('toggle-sidebar')
}

const handleItemClick = async (item) => {
	if (!item.hasSubmenu) {
		resetAllActiveStates()
		item.active = true
		try {
			await router.push(item.route)
			emit('navigate', { type: 'main', route: item.route, item })
		} catch (error) {
			console.error('Navigation error:', error)
		}
		return
	}

	const wasActive = item.active
	resetAllActiveStates()
	item.active = !wasActive

	if (item.active && item.route) {
		try {
			await router.push(item.route)
			emit('navigate', { type: 'main', route: item.route, item })
		} catch (error) {
			console.error('Navigation error:', error)
		}
	}
}

const handleSubmenuClick = async (parentItem, submenu) => {
	if (parentItem.submenu) {
		parentItem.submenu.forEach((sub) => {
			sub.active = false
		})
	}
	submenu.active = true
	try {
		await router.push(submenu.route)
		emit('navigate', {
			type: 'submenu',
			route: submenu.route,
			submenu,
			parentItem,
		})
	} catch (error) {
		console.error('Navigation error:', error)
	}
}

const resetAllActiveStates = () => {
	sidebarItems.value.forEach((item) => {
		item.active = false
		if (item.submenu) {
			item.submenu.forEach((sub) => {
				sub.active = false
			})
		}
	})
}

const setActiveBasedOnRoute = () => {
	const currentPath = route.path
	sidebarItems.value.forEach((item) => {
		if (currentPath === item.route) {
			resetAllActiveStates()
			item.active = true
			return
		}
		if (item.submenu) {
			const activeSubmenu = item.submenu.find((sub) => currentPath === sub.route)
			if (activeSubmenu) {
				resetAllActiveStates()
				item.active = true
				activeSubmenu.active = true
				return
			}
		}
	})
}

const handleResize = () => {
	if (window.innerWidth < 768) {
		emit('toggle-sidebar', false)
	}
}

// Watch for route changes
onMounted(() => {
	handleResize()
	setActiveBasedOnRoute() // Only activates current route item
	window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
	window.removeEventListener('resize', handleResize)
})

import { watch } from 'vue'
watch(
	() => route.path,
	() => {
		setActiveBasedOnRoute()
	},
)
</script>

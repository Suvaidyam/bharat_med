<!-- components/Topbar.vue -->
<template>
	<header class="bg-white border-b border-gray-200 px-6 py-4">
		<div class="flex items-center justify-between">
			<div>
				<h1 class="text-2xl font-semibold text-gray-900">
					{{ title }}
				</h1>
				<!-- <p class="text-gray-600 mt-1">
					{{ subtitle }}
				</p> -->
			</div>
			<div class="flex items-center space-x-4">
				<SearchIcon class="w-5 h-5 text-gray-400 cursor-pointer hover:text-gray-600" />
				<div class="relative">
					<BellIcon class="w-5 h-5 text-gray-400 cursor-pointer hover:text-gray-600" />
					<div
						v-if="hasNotifications"
						class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"
					></div>
				</div>
				<!-- Login Dropdown -->
				<div v-if="session?.isLoggedIn">
					<Dropdown
						:options="dropdownOptions"
						:button="{
							label: userInitial,
						}"
					/>
				</div>
			</div>
		</div>
	</header>
</template>

<script setup>
import { computed, inject } from 'vue'
import { SearchIcon, BellIcon } from 'lucide-vue-next'
import { Dropdown } from 'frappe-ui'

// Props
const props = defineProps({
	title: {
		type: String,
		default: 'Welcome back, Dr. AJ',
	},
	// subtitle: {
	// 	type: String,
	// 	default: "Here's what's happening with your patients today.",
	// },
	hasNotifications: {
		type: Boolean,
		default: true,
	},
})

// Emits
const emit = defineEmits(['profile-click', 'logout', 'search', 'notifications'])

// Session injection
const session = inject('$session')

// Computed
const userInitial = computed(() => {
	return session?.user?.charAt(0).toUpperCase() || 'U'
})

const dropdownOptions = computed(() => [
	{
		label: 'Profile',
		onClick: () => emit('profile-click'),
	},
	{
		label: 'Logout',
		onClick: () => {
			if (session?.logout?.submit) {
				session.logout.submit()
			}
			emit('logout')
		},
	},
])
</script>

<template>
	<div class="min-h-screen bg-gray-50 p-4 lg:p-6">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex items-center gap-3 mb-2">
				<button class="p-1 hover:bg-gray-100 rounded-md">
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
							d="M15 19l-7-7 7-7"
						/>
					</svg>
				</button>
				<h1 class="text-2xl font-semibold text-gray-900">Roles & Permissions</h1>
			</div>
			<p class="text-gray-500 text-sm">Manage staff access and security controls</p>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
			<!-- Total Roles -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Total Roles</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">8</div>
				<div class="text-sm text-gray-500">6 default, 2 custom</div>
			</div>

			<!-- Staff Assigned -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Staff Assigned</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">53</div>
				<div class="text-sm text-gray-500">Across all roles</div>
			</div>

			<!-- Medical Roles -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Medical Roles</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">3</div>
				<div class="text-sm text-gray-500">30 staff assigned</div>
			</div>

			<!-- Permission Sets -->
			<div class="bg-white rounded-lg p-6 shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<h3 class="text-sm font-medium text-gray-600">Permission Sets</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">8</div>
				<div class="text-sm text-gray-500">4 permission types</div>
			</div>
		</div>

		<!-- Main Content -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<!-- Tabs -->
			<div class="border-b border-gray-200 px-6">
				<nav class="flex space-x-8">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'py-4 px-1 border-b-2 font-medium text-sm transition-colors',
							activeTab === tab.id
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
						]"
					>
						{{ tab.name }}
					</button>
				</nav>
			</div>

			<!-- Search and Actions -->
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col sm:flex-row gap-4 justify-between">
					<div class="flex-1 max-w-md">
						<div class="relative">
							<svg
								class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								/>
							</svg>
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search roles..."
								class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
							/>
							<button
								class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-gray-600"
							>
								<svg
									class="w-4 h-4"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
									/>
								</svg>
							</button>
						</div>
					</div>
					<div class="flex gap-3">
						<button
							class="px-4 py-2 text-gray-600 hover:text-gray-800 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center gap-2"
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								/>
							</svg>
							Export
						</button>
						<button
							class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
						>
							<svg
								class="w-4 h-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 4v16m8-8H4"
								/>
							</svg>
							Add Role
						</button>
					</div>
				</div>
			</div>

			<!-- Role Categories -->
			<div class="px-6 py-4 border-b border-gray-200">
				<div class="flex flex-wrap gap-2">
					<button
						v-for="category in categories"
						:key="category.id"
						@click="activeCategory = category.id"
						:class="[
							'px-3 py-1 rounded-full text-sm font-medium transition-colors',
							activeCategory === category.id
								? 'bg-blue-100 text-blue-700'
								: 'bg-gray-100 text-gray-600 hover:bg-gray-200',
						]"
					>
						{{ category.name }}
					</button>
				</div>
			</div>

			<!-- Roles Table -->
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Role Name
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Category
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Description
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Users
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Last Updated
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Actions
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr v-for="role in filteredRoles" :key="role.id" class="hover:bg-gray-50">
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div class="text-sm font-medium text-gray-900">
										{{ role.name }}
									</div>
									<span
										v-if="role.isDefault"
										class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800"
									>
										Default
									</span>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="[
										'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium',
										role.category === 'Medical'
											? 'bg-green-100 text-green-800'
											: 'bg-blue-100 text-blue-800',
									]"
								>
									{{ role.category }}
								</span>
							</td>
							<td class="px-6 py-4">
								<div class="text-sm text-gray-900">{{ role.description }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ role.users }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ role.lastUpdated }}</div>
								<div class="text-sm text-gray-500">by {{ role.updatedBy }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
								<button class="text-gray-400 hover:text-gray-600 p-1">
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
										<path
											d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
										/>
									</svg>
								</button>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const activeTab = ref('Roles')
const activeCategory = ref('All Roles')
const searchQuery = ref('')

// Static data
const tabs = [
	{ id: 'Roles', name: 'Roles' },
	{ id: 'Templates', name: 'Templates' },
	{ id: 'Permission Matrix', name: 'Permission Matrix' },
	{ id: 'Audit Logs', name: 'Audit Logs' },
]

const categories = [
	{ id: 'All Roles', name: 'All Roles' },
	{ id: 'Medical', name: 'Medical' },
	{ id: 'Administrative', name: 'Administrative' },
	{ id: 'Custom', name: 'Custom' },
]

const roles = ref([
	{
		id: 1,
		name: 'Administrator',
		category: 'Administrative',
		description: 'Full system access with all permissions',
		users: 3,
		lastUpdated: '2023-11-15',
		updatedBy: 'System Admin',
		isDefault: true,
	},
	{
		id: 2,
		name: 'Doctor',
		category: 'Medical',
		description: 'Access to patient records, appointments, and prescriptions',
		users: 12,
		lastUpdated: '2023-10-22',
		updatedBy: 'System Admin',
		isDefault: true,
	},
	{
		id: 3,
		name: 'Nurse',
		category: 'Medical',
		description: 'Limited access to patient records and appointments',
		users: 18,
		lastUpdated: '2023-09-30',
		updatedBy: 'Dr. Sarah Johnson',
		isDefault: true,
	},
	{
		id: 4,
		name: 'Receptionist',
		category: 'Administrative',
		description: 'Manage appointments and patient registration',
		users: 5,
		lastUpdated: '2023-10-05',
		updatedBy: 'Dr. Sarah Johnson',
		isDefault: true,
	},
	{
		id: 5,
		name: 'Billing Staff',
		category: 'Administrative',
		description: 'Manage billing and payments',
		users: 4,
		lastUpdated: '2023-11-02',
		updatedBy: 'System Admin',
		isDefault: true,
	},
])

// Computed properties
const filteredRoles = computed(() => {
	let filtered = roles.value

	// Filter by category
	if (activeCategory.value !== 'All Roles') {
		filtered = filtered.filter((role) => role.category === activeCategory.value)
	}

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(role) =>
				role.name.toLowerCase().includes(query) ||
				role.description.toLowerCase().includes(query) ||
				role.category.toLowerCase().includes(query),
		)
	}

	return filtered
})
</script>

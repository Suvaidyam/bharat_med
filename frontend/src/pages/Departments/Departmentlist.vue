<template>
	<div class="min-h-screen p-4 md:p-6">
		<div class="">
			<!-- Header -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">Departments</h1>
					<p class="text-gray-600">
						Manage your clinic's departments and staff assignments
					</p>
				</div>
				<button
					class="mt-4 sm:mt-0 bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
				>
					<span class="text-lg">+</span>
					Add Department
				</button>
			</div>

			<!-- Statistics Cards -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
				<!-- Total Departments Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Total Departments</h3>
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
									d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
								></path>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">
						{{ stats.totalDepartments }}
					</div>
					<div class="text-sm text-gray-500">+2 from last month</div>
				</div>

				<!-- Total Staff Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Total Staff</h3>
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
									d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"
								></path>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">{{ stats.totalStaff }}</div>
					<div class="text-sm text-gray-500">+4 from last month</div>
				</div>

				<!-- Services Offered Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Services Offered</h3>
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
									d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
								></path>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">
						{{ stats.servicesOffered }}
					</div>
					<div class="text-sm text-gray-500">+10 from last month</div>
				</div>
			</div>

			<!-- Department List Section -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-100">
				<!-- Section Header -->
				<div class="p-6 border-b border-gray-100">
					<div
						class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
					>
						<div>
							<h2 class="text-lg font-semibold text-gray-900 mb-1">
								Department List
							</h2>
							<p class="text-sm text-gray-600">
								View and manage all departments in your clinic
							</p>
						</div>
						<div class="relative">
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search departments..."
								class="pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
							/>
							<svg
								class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 transform -translate-y-1/2"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
								></path>
							</svg>
						</div>
					</div>
				</div>

				<!-- Filter Tabs -->
				<div class="px-6 py-4 border-b border-gray-100">
					<div class="flex gap-6">
						<button
							v-for="tab in tabs"
							:key="tab.key"
							@click="activeTab = tab.key"
							:class="[
								'text-sm font-medium pb-2 border-b-2 transition-colors',
								activeTab === tab.key
									? 'text-blue-600 border-blue-600'
									: 'text-gray-500 border-transparent hover:text-gray-700',
							]"
						>
							{{ tab.label }}
						</button>
					</div>
				</div>

				<!-- Table -->
				<div class="overflow-x-auto">
					<table class="w-full">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Department Name
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Head of Department
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Staff Count
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Services
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Actions
								</th>
							</tr>
						</thead>
						<tbody class="bg-white divide-y divide-gray-200">
							<tr
								v-for="department in filteredDepartments"
								:key="department.id"
								class="hover:bg-gray-50"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ department.name }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div
										class="text-sm text-blue-600 hover:text-blue-800 cursor-pointer"
									>
										{{ department.head }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ department.staffCount }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ department.services }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="[
											'inline-flex px-2 py-1 text-xs font-medium rounded-full',
											department.status === 'Active'
												? 'bg-green-100 text-green-800'
												: 'bg-yellow-100 text-yellow-800',
										]"
									>
										{{ department.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<button class="text-gray-400 hover:text-gray-600">
										<svg
											class="w-5 h-5"
											fill="currentColor"
											viewBox="0 0 20 20"
										>
											<path
												d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
											></path>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchQuery = ref('')
const activeTab = ref('all')

// Statistics data
const stats = ref({
	totalDepartments: 12,
	totalStaff: 48,
	servicesOffered: 86,
})

// Tab configuration
const tabs = ref([
	{ key: 'all', label: 'All Departments' },
	{ key: 'active', label: 'Active' },
	{ key: 'inactive', label: 'Inactive' },
])

// Departments data
const departments = ref([
	{
		id: 1,
		name: 'Cardiology',
		head: 'Dr. Sarah Johnson',
		staffCount: 8,
		services: 12,
		status: 'Active',
	},
	{
		id: 2,
		name: 'Neurology',
		head: 'Dr. Michael Chen',
		staffCount: 6,
		services: 9,
		status: 'Active',
	},
	{
		id: 3,
		name: 'Pediatrics',
		head: 'Dr. Emily Rodriguez',
		staffCount: 10,
		services: 15,
		status: 'Active',
	},
	{
		id: 4,
		name: 'Orthopedics',
		head: 'Dr. James Wilson',
		staffCount: 7,
		services: 11,
		status: 'Active',
	},
	{
		id: 5,
		name: 'Dermatology',
		head: 'Dr. Lisa Thompson',
		staffCount: 4,
		services: 8,
		status: 'Active',
	},
	{
		id: 6,
		name: 'Ophthalmology',
		head: 'Dr. Robert Kim',
		staffCount: 5,
		services: 7,
		status: 'Active',
	},
	{
		id: 7,
		name: 'Psychiatry',
		head: 'Dr. Jennifer Martinez',
		staffCount: 6,
		services: 10,
		status: 'Active',
	},
	{
		id: 8,
		name: 'Radiology',
		head: 'Dr. David Brown',
		staffCount: 4,
		services: 6,
		status: 'Inactive',
	},
	{
		id: 9,
		name: 'Oncology',
		head: 'Dr. Susan Lee',
		staffCount: 7,
		services: 9,
		status: 'Active',
	},
	{
		id: 10,
		name: 'Endocrinology',
		head: 'Dr. Thomas Garcia',
		staffCount: 3,
		services: 5,
		status: 'Inactive',
	},
])

// Computed properties
const filteredDepartments = computed(() => {
	let filtered = departments.value

	// Filter by active tab
	if (activeTab.value === 'active') {
		filtered = filtered.filter((dept) => dept.status === 'Active')
	} else if (activeTab.value === 'inactive') {
		filtered = filtered.filter((dept) => dept.status === 'Inactive')
	}

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(dept) =>
				dept.name.toLowerCase().includes(query) || dept.head.toLowerCase().includes(query),
		)
	}

	return filtered
})
</script>

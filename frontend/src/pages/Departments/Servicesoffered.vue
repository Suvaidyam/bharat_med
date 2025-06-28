<template>
	<div class="min-h-screen p-4 md:p-6">
		<div class="">
			<!-- Header -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">
						Services Offered
					</h1>
					<p class="text-gray-600">
						Manage and view all services offered across departments
					</p>
				</div>
				<button
					class="mt-4 sm:mt-0 bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
				>
					<span class="text-lg">+</span>
					Add New Service
				</button>
			</div>

			<!-- Statistics Cards -->
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
				<!-- Total Services Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Total Services</h3>
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
								></path>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">
						{{ stats.totalServices }}
					</div>
					<div class="text-sm text-gray-500">
						Across {{ stats.departments }} departments
					</div>
				</div>

				<!-- Most Popular Service Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Most Popular</h3>
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
									d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
								></path>
							</svg>
						</div>
					</div>
					<div class="text-lg font-bold text-gray-900 mb-1">
						{{ stats.mostPopular.name }}
					</div>
					<div class="text-sm text-gray-500">
						{{ stats.mostPopular.appointments }} appointments this month
					</div>
				</div>

				<!-- Average Duration Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Average Duration</h3>
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
									d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
								></path>
							</svg>
						</div>
					</div>
					<div class="text-3xl font-bold text-gray-900 mb-1">
						{{ stats.avgDuration }} min
					</div>
					<div class="text-sm text-gray-500">Across all services</div>
				</div>

				<!-- Monthly Revenue Card -->
				<div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
					<div class="flex items-center justify-between mb-4">
						<h3 class="text-sm font-medium text-gray-600">Monthly Revenue</h3>
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
						{{ formatCurrency(stats.monthlyRevenue) }}
					</div>
					<div class="text-sm text-gray-500">+15% from last month</div>
				</div>
			</div>

			<!-- Services List Section -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-100">
				<!-- Section Header with Search and Filters -->
				<div class="p-6 border-b border-gray-100">
					<div
						class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4"
					>
						<div class="relative flex-1 max-w-md">
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search services..."
								class="pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full"
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

						<div class="flex flex-col sm:flex-row gap-3">
							<!-- Department Filter -->
							<select
								v-model="selectedDepartment"
								class="px-3 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">All Departments</option>
								<option v-for="dept in departments" :key="dept" :value="dept">
									{{ dept }}
								</option>
							</select>

							<!-- Filter Button -->
							<button
								class="flex items-center gap-2 px-3 py-2 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
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
										d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.707A1 1 0 013 7V4z"
									></path>
								</svg>
								Filter
							</button>
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

				<!-- Services Header -->
				<div class="px-6 py-4 border-b border-gray-100">
					<h2 class="text-lg font-semibold text-gray-900 mb-1">All Services</h2>
					<p class="text-sm text-gray-600">
						Showing all {{ filteredServices.length }} services across all departments
					</p>
				</div>

				<!-- Table -->
				<div class="overflow-x-auto">
					<table class="w-full">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Service Name
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Department
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Type
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Duration
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Price
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
								v-for="service in paginatedServices"
								:key="service.id"
								class="hover:bg-gray-50"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ service.name }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div
										class="text-sm text-blue-600 hover:text-blue-800 cursor-pointer"
									>
										{{ service.department }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="[
											'inline-flex px-2 py-1 text-xs font-medium rounded-full',
											getTypeColor(service.type),
										]"
									>
										{{ service.type }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ service.duration }} min
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">${{ service.price }}</div>
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

				<!-- Pagination -->
				<div class="px-6 py-4 border-t border-gray-100 flex items-center justify-between">
					<div class="text-sm text-gray-500">
						Showing {{ (currentPage - 1) * itemsPerPage + 1 }} of
						{{ filteredServices.length }} services
					</div>
					<div class="flex items-center gap-2">
						<button
							@click="currentPage--"
							:disabled="currentPage === 1"
							:class="[
								'px-3 py-1 text-sm rounded border',
								currentPage === 1
									? 'text-gray-400 border-gray-200 cursor-not-allowed'
									: 'text-gray-600 border-gray-300 hover:bg-gray-50',
							]"
						>
							Previous
						</button>
						<button
							@click="currentPage++"
							:disabled="currentPage === totalPages"
							:class="[
								'px-3 py-1 text-sm rounded border',
								currentPage === totalPages
									? 'text-gray-400 border-gray-200 cursor-not-allowed'
									: 'text-gray-600 border-gray-300 hover:bg-gray-50',
							]"
						>
							Next
						</button>
					</div>
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
const selectedDepartment = ref('')
const currentPage = ref(1)
const itemsPerPage = 7

// Statistics data
const stats = ref({
	totalServices: 86,
	departments: 12,
	mostPopular: {
		name: 'General Checkup',
		appointments: 182,
	},
	avgDuration: 45,
	monthlyRevenue: 128450,
})

// Tab configuration
const tabs = ref([
	{ key: 'all', label: 'All' },
	{ key: 'diagnostic', label: 'Diagnostic' },
	{ key: 'treatment', label: 'Treatment' },
	{ key: 'preventive', label: 'Preventive' },
])

// Departments for filter
const departments = ref([
	'General Medicine',
	'Cardiology',
	'Radiology',
	'Orthopedics',
	'Pediatrics',
	'Neurology',
	'Laboratory',
])

// Services data
const services = ref([
	{
		id: 1,
		name: 'General Checkup',
		department: 'General Medicine',
		type: 'Preventive',
		duration: 30,
		price: 75,
	},
	{
		id: 2,
		name: 'ECG',
		department: 'Cardiology',
		type: 'Diagnostic',
		duration: 20,
		price: 120,
	},
	{
		id: 3,
		name: 'MRI Scan',
		department: 'Radiology',
		type: 'Diagnostic',
		duration: 45,
		price: 850,
	},
	{
		id: 4,
		name: 'Physical Therapy Session',
		department: 'Orthopedics',
		type: 'Treatment',
		duration: 60,
		price: 95,
	},
	{
		id: 5,
		name: 'Vaccination',
		department: 'Pediatrics',
		type: 'Preventive',
		duration: 15,
		price: 65,
	},
	{
		id: 6,
		name: 'Neurological Assessment',
		department: 'Neurology',
		type: 'Diagnostic',
		duration: 60,
		price: 225,
	},
	{
		id: 7,
		name: 'Blood Test',
		department: 'Laboratory',
		type: 'Diagnostic',
		duration: 10,
		price: 45,
	},
	{
		id: 8,
		name: 'X-Ray',
		department: 'Radiology',
		type: 'Diagnostic',
		duration: 15,
		price: 125,
	},
	{
		id: 9,
		name: 'Ultrasound',
		department: 'Radiology',
		type: 'Diagnostic',
		duration: 30,
		price: 180,
	},
	{
		id: 10,
		name: 'Cardiac Stress Test',
		department: 'Cardiology',
		type: 'Diagnostic',
		duration: 45,
		price: 275,
	},
])

// Computed properties
const filteredServices = computed(() => {
	let filtered = services.value

	// Filter by active tab
	if (activeTab.value !== 'all') {
		filtered = filtered.filter(
			(service) => service.type.toLowerCase() === activeTab.value.toLowerCase(),
		)
	}

	// Filter by department
	if (selectedDepartment.value) {
		filtered = filtered.filter((service) => service.department === selectedDepartment.value)
	}

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(service) =>
				service.name.toLowerCase().includes(query) ||
				service.department.toLowerCase().includes(query),
		)
	}

	return filtered
})

const totalPages = computed(() => Math.ceil(filteredServices.value.length / itemsPerPage))

const paginatedServices = computed(() => {
	const start = (currentPage.value - 1) * itemsPerPage
	const end = start + itemsPerPage
	return filteredServices.value.slice(start, end)
})

// Methods
const formatCurrency = (amount) => {
	return new Intl.NumberFormat('en-US', {
		style: 'currency',
		currency: 'USD',
		minimumFractionDigits: 0,
	}).format(amount)
}

const getTypeColor = (type) => {
	const colors = {
		Preventive: 'bg-green-100 text-green-800',
		Diagnostic: 'bg-blue-100 text-blue-800',
		Treatment: 'bg-purple-100 text-purple-800',
	}
	return colors[type] || 'bg-gray-100 text-gray-800'
}

// Watch for tab changes to reset pagination
import { watch } from 'vue'
watch([activeTab, selectedDepartment, searchQuery], () => {
	currentPage.value = 1
})
</script>

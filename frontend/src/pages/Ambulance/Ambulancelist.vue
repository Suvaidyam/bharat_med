<template>
	<div class="min-h-screen p-4 sm:p-6">
		<div class="">
			<!-- Header -->
			<div
				class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6"
			>
				<div>
					<h1 class="text-2xl font-bold text-gray-900 mb-1">Ambulance List</h1>
					<p class="text-gray-600">Manage and track all ambulances in the fleet</p>
				</div>
				<button
					@click="showNewAmbulanceModal = true"
					class="mt-4 sm:mt-0 bg-gray-900 text-white px-4 py-2 rounded-sm hover:bg-gray-800 transition-colors flex items-center"
				>
					<svg
						class="w-4 h-4 mr-2"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 6v6m0 0v6m0-6h6m-6 0H6"
						/>
					</svg>
					Add New Ambulance
				</button>
			</div>

			<!-- Stats Cards -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
				<!-- Total Ambulances -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">Total Ambulances</p>
							<p class="text-3xl font-bold text-gray-900">
								{{ stats.totalAmbulances }}
							</p>
							<p class="text-sm text-gray-500 mt-1">
								{{ stats.totalAmbulancesChange }}
							</p>
						</div>
						<div class="p-3 bg-blue-50 rounded-lg">
							<svg
								class="w-6 h-6 text-blue-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0M15 17a2 2 0 104 0"
								/>
							</svg>
						</div>
					</div>
				</div>

				<!-- Available Ambulances -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">
								Available Ambulances
							</p>
							<p class="text-3xl font-bold text-gray-900">
								{{ stats.availableAmbulances }}
							</p>
							<p class="text-sm text-gray-500 mt-1">
								{{ stats.availableAmbulancesStatus }}
							</p>
						</div>
						<div class="p-3 bg-green-50 rounded-lg">
							<svg
								class="w-6 h-6 text-green-600"
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
				</div>

				<!-- Maintenance Due -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">Maintenance Due</p>
							<p class="text-3xl font-bold text-gray-900">
								{{ stats.maintenanceDue }}
							</p>
							<p class="text-sm text-gray-500 mt-1">
								{{ stats.maintenanceDueSchedule }}
							</p>
						</div>
						<div class="p-3 bg-orange-50 rounded-lg">
							<svg
								class="w-6 h-6 text-orange-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								/>
							</svg>
						</div>
					</div>
				</div>
			</div>

			<!-- Ambulance Fleet Section -->
			<div class="bg-white rounded-sm shadow-sm border border-gray-200">
				<div class="p-6 border-b border-gray-200">
					<h2 class="text-lg font-semibold text-gray-900 mb-1">Ambulance Fleet</h2>
					<p class="text-gray-600">View and manage all ambulances in your fleet</p>
				</div>

				<!-- Filters and Search -->
				<div class="p-6 border-b border-gray-200">
					<div class="flex flex-col lg:flex-row gap-4">
						<!-- Search -->
						<div class="relative flex-1 max-w-md">
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
								placeholder="Search ambulances..."
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full"
							/>
						</div>

						<!-- Filters -->
						<div class="flex flex-wrap gap-2">
							<select
								v-model="statusFilter"
								class="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">All Statuses</option>
								<option value="Available">Available</option>
								<option value="On Call">On Call</option>
								<option value="Maintenance">Maintenance</option>
							</select>

							<select
								v-model="typeFilter"
								class="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="">All Types</option>
								<option value="Basic Life Support">Basic Life Support</option>
								<option value="Advanced Life Support">
									Advanced Life Support
								</option>
								<option value="Patient Transport">Patient Transport</option>
							</select>
						</div>
					</div>
				</div>

				<!-- Status Tabs -->
				<div class="px-6 pt-4">
					<div class="flex space-x-1">
						<button
							v-for="tab in statusTabs"
							:key="tab.key"
							@click="activeTab = tab.key"
							:class="[
								'px-4 py-2 text-sm font-medium rounded-lg transition-colors',
								activeTab === tab.key
									? 'bg-blue-100 text-blue-700'
									: 'text-gray-500 hover:text-gray-700 hover:bg-gray-100',
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
									ID
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Registration
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Model
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Type
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Driver
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Location
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
								v-for="ambulance in filteredAmbulances"
								:key="ambulance.id"
								class="hover:bg-gray-50"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ ambulance.id }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ ambulance.registration }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ ambulance.model.name }}
									</div>
									<div class="text-sm text-gray-500">
										{{ ambulance.model.year }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">{{ ambulance.type }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getStatusBadgeClass(ambulance.status)"
										class="px-2 py-1 text-xs font-medium rounded-full"
									>
										{{ ambulance.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">{{ ambulance.driver }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ ambulance.location }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<button class="text-gray-400 hover:text-gray-600">
										<svg
											class="w-4 h-4"
											fill="currentColor"
											viewBox="0 0 20 20"
										>
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

		<!-- New Ambulance Modal (placeholder) -->
		<div
			v-if="showNewAmbulanceModal"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
		>
			<div class="bg-white rounded-sm max-w-md w-full p-6">
				<h3 class="text-lg font-semibold mb-4">Add New Ambulance</h3>
				<p class="text-gray-600 mb-4">
					This would contain a form to add a new ambulance to the fleet.
				</p>
				<div class="flex justify-end space-x-2">
					<button
						@click="showNewAmbulanceModal = false"
						class="px-4 py-2 text-gray-600 hover:text-gray-800"
					>
						Cancel
					</button>
					<button
						@click="showNewAmbulanceModal = false"
						class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
					>
						Add Ambulance
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchQuery = ref('')
const statusFilter = ref('')
const typeFilter = ref('')
const activeTab = ref('all')
const showNewAmbulanceModal = ref(false)

// Stats data
const stats = ref({
	totalAmbulances: 7,
	totalAmbulancesChange: '+1 from last month',
	availableAmbulances: 4,
	availableAmbulancesStatus: '2 on call, 1 in maintenance',
	maintenanceDue: 2,
	maintenanceDueSchedule: 'Next scheduled: May 20, 2023',
})

// Status tabs
const statusTabs = ref([
	{ key: 'all', label: 'All' },
	{ key: 'available', label: 'Available' },
	{ key: 'on-call', label: 'On Call' },
	{ key: 'maintenance', label: 'Maintenance' },
])

// Mock data for ambulances
const ambulances = ref([
	{
		id: 'AMB-001',
		registration: 'XYZ-1234',
		model: { name: 'Toyota HiAce', year: '2021' },
		type: 'Basic Life Support',
		status: 'Available',
		driver: 'Michael Johnson',
		location: 'Main Hospital',
	},
	{
		id: 'AMB-002',
		registration: 'ABC-5678',
		model: { name: 'Mercedes Sprinter', year: '2022' },
		type: 'Advanced Life Support',
		status: 'On Call',
		driver: 'Sarah Wilson',
		location: 'East Wing',
	},
	{
		id: 'AMB-003',
		registration: 'DEF-9012',
		model: { name: 'Ford Transit', year: '2020' },
		type: 'Basic Life Support',
		status: 'Available',
		driver: 'Robert Davis',
		location: 'North Clinic',
	},
	{
		id: 'AMB-004',
		registration: 'GHI-3456',
		model: { name: 'Fiat Ducato', year: '2019' },
		type: 'Patient Transport',
		status: 'Maintenance',
		driver: 'Thomas Anderson',
		location: 'Workshop',
	},
	{
		id: 'AMB-005',
		registration: 'JKL-7890',
		model: { name: 'Volkswagen Crafter', year: '2021' },
		type: 'Advanced Life Support',
		status: 'Available',
		driver: 'Jennifer Lopez',
		location: 'South Clinic',
	},
	{
		id: 'AMB-006',
		registration: 'MNO-1234',
		model: { name: 'Renault Master', year: '2020' },
		type: 'Basic Life Support',
		status: 'On Call',
		driver: 'David Miller',
		location: 'West Wing',
	},
	{
		id: 'AMB-007',
		registration: 'PQR-5678',
		model: { name: 'Mercedes Sprinter', year: '2022' },
		type: 'Advanced Life Support',
		status: 'Available',
		driver: 'Emily Clark',
		location: 'Main Hospital',
	},
])

// Computed properties
const filteredAmbulances = computed(() => {
	let filtered = ambulances.value

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(ambulance) =>
				ambulance.id.toLowerCase().includes(query) ||
				ambulance.registration.toLowerCase().includes(query) ||
				ambulance.model.name.toLowerCase().includes(query) ||
				ambulance.driver.toLowerCase().includes(query) ||
				ambulance.location.toLowerCase().includes(query),
		)
	}

	// Filter by status
	if (statusFilter.value) {
		filtered = filtered.filter((ambulance) => ambulance.status === statusFilter.value)
	}

	// Filter by type
	if (typeFilter.value) {
		filtered = filtered.filter((ambulance) => ambulance.type === typeFilter.value)
	}

	// Filter by active tab
	if (activeTab.value !== 'all') {
		const tabStatusMap = {
			available: 'Available',
			'on-call': 'On Call',
			maintenance: 'Maintenance',
		}
		filtered = filtered.filter(
			(ambulance) => ambulance.status === tabStatusMap[activeTab.value],
		)
	}

	return filtered
})

// Methods
const getStatusBadgeClass = (status) => {
	const classes = {
		Available: 'bg-green-100 text-green-800',
		'On Call': 'bg-blue-100 text-blue-800',
		Maintenance: 'bg-orange-100 text-orange-800',
	}
	return classes[status] || 'bg-gray-100 text-gray-800'
}
</script>

<template>
	<div class="min-h-screen p-4 sm:p-6">
		<div class="">
			<!-- Header -->
			<div
				class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6"
			>
				<div>
					<h1 class="text-2xl font-bold text-gray-900 mb-1">Ambulance Call List</h1>
					<p class="text-gray-600">
						Manage and track all ambulance calls and dispatches
					</p>
				</div>
				<button
					@click="showNewCallModal = true"
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
					New Ambulance Call
				</button>
			</div>

			<!-- Stats Cards -->
			<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
				<!-- Total Calls -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">Total Calls</p>
							<p class="text-3xl font-bold text-gray-900">{{ stats.totalCalls }}</p>
							<p class="text-sm text-gray-500 mt-1">
								{{ stats.totalCallsChange }} from last month
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
									d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
								/>
							</svg>
						</div>
					</div>
				</div>

				<!-- Active Calls -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">Active Calls</p>
							<p class="text-3xl font-bold text-gray-900">{{ stats.activeCalls }}</p>
							<p class="text-sm text-gray-500 mt-1">{{ stats.activeCallsStatus }}</p>
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
									d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
								/>
							</svg>
						</div>
					</div>
				</div>

				<!-- Average Response Time -->
				<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
					<div class="flex items-center justify-between">
						<div>
							<p class="text-sm font-medium text-gray-600 mb-1">
								Average Response Time
							</p>
							<p class="text-3xl font-bold text-gray-900">
								{{ stats.avgResponseTime }}
							</p>
							<p class="text-sm text-gray-500 mt-1">
								{{ stats.avgResponseTimeChange }} from last month
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
									d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
						</div>
					</div>
				</div>
			</div>

			<!-- Ambulance Calls Section -->
			<div class="bg-white rounded-sm shadow-sm border border-gray-200">
				<div class="p-6 border-b border-gray-200">
					<h2 class="text-lg font-semibold text-gray-900 mb-1">Ambulance Calls</h2>
					<p class="text-gray-600">View and manage all ambulance calls and dispatches</p>
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
								placeholder="Search calls..."
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
								<option value="Pending">Pending</option>
								<option value="In Progress">In Progress</option>
								<option value="Completed">Completed</option>
							</select>

							<select
								v-model="dateFilter"
								class="px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							>
								<option value="today">Today</option>
								<option value="week">This Week</option>
								<option value="month">This Month</option>
								<option value="all">All Time</option>
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
									Call ID
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Date & Time
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Patient
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Location
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Reason
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Ambulance
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
								v-for="call in filteredCalls"
								:key="call.id"
								class="hover:bg-gray-50"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ call.id }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">{{ call.date }}</div>
									<div class="text-sm text-gray-500">{{ call.time }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ call.patient.name }}
									</div>
									<div class="text-sm text-gray-500">
										{{ call.patient.phone }}
									</div>
								</td>
								<td class="px-6 py-4">
									<div class="text-sm text-gray-900">{{ call.location }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">{{ call.reason }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getStatusBadgeClass(call.status)"
										class="px-2 py-1 text-xs font-medium rounded-full"
									>
										{{ call.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm font-medium text-gray-900">
										{{ call.ambulance.id }}
									</div>
									<div class="text-sm text-gray-500">
										{{ call.ambulance.driver }}
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

		<!-- New Call Modal (placeholder) -->
		<div
			v-if="showNewCallModal"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
		>
			<div class="bg-white rounded-sm max-w-md w-full p-6">
				<h3 class="text-lg font-semibold mb-4">New Ambulance Call</h3>
				<p class="text-gray-600 mb-4">
					This would contain a form to create a new ambulance call.
				</p>
				<div class="flex justify-end space-x-2">
					<button
						@click="showNewCallModal = false"
						class="px-4 py-2 text-gray-600 hover:text-gray-800"
					>
						Cancel
					</button>
					<button
						@click="showNewCallModal = false"
						class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
					>
						Create Call
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
const dateFilter = ref('today')
const activeTab = ref('all')
const showNewCallModal = ref(false)

// Stats data
const stats = ref({
	totalCalls: 127,
	totalCallsChange: '+5.3% from last month',
	activeCalls: 3,
	activeCallsStatus: '2 pending, 1 in progress',
	avgResponseTime: '8.5 min',
	avgResponseTimeChange: '-1.2 min from last month',
})

// Status tabs
const statusTabs = ref([
	{ key: 'all', label: 'All' },
	{ key: 'pending', label: 'Pending' },
	{ key: 'in-progress', label: 'In Progress' },
	{ key: 'completed', label: 'Completed' },
])

// Mock data for calls
const calls = ref([
	{
		id: 'AC001',
		date: '2023-04-22',
		time: '08:30 AM',
		patient: { name: 'John Doe', phone: '+1 (555) 123-4567' },
		location: '123 Main St, Anytown',
		reason: 'Chest Pain',
		status: 'Completed',
		ambulance: { id: 'AMB-001', driver: 'Michael Johnson' },
	},
	{
		id: 'AC002',
		date: '2023-04-22',
		time: '09:45 AM',
		patient: { name: 'Jane Smith', phone: '+1 (555) 987-6543' },
		location: '456 Oak Ave, Somewhere',
		reason: 'Traffic Accident',
		status: 'In Progress',
		ambulance: { id: 'AMB-003', driver: 'Robert Davis' },
	},
	{
		id: 'AC003',
		date: '2023-04-22',
		time: '11:15 AM',
		patient: { name: 'Emily Johnson', phone: '+1 (555) 456-7890' },
		location: '789 Pine Rd, Elsewhere',
		reason: 'Difficulty Breathing',
		status: 'Pending',
		ambulance: { id: 'AMB-002', driver: 'Sarah Wilson' },
	},
	{
		id: 'AC004',
		date: '2023-04-21',
		time: '02:30 PM',
		patient: { name: 'David Brown', phone: '+1 (555) 234-5678' },
		location: '321 Elm St, Nowhere',
		reason: 'Fall Injury',
		status: 'Completed',
		ambulance: { id: 'AMB-001', driver: 'Michael Johnson' },
	},
	{
		id: 'AC005',
		date: '2023-04-21',
		time: '05:00 PM',
		patient: { name: 'Lisa Garcia', phone: '+1 (555) 876-5432' },
		location: '654 Maple Dr, Anytown',
		reason: 'Stroke Symptoms',
		status: 'Completed',
		ambulance: { id: 'AMB-004', driver: 'Thomas Anderson' },
	},
	{
		id: 'AC006',
		date: '2023-04-21',
		time: '07:45 PM',
		patient: { name: 'Robert Martinez', phone: '+1 (555) 345-6789' },
		location: '987 Cedar Ln, Somewhere',
		reason: 'Severe Allergic Reaction',
		status: 'Completed',
		ambulance: { id: 'AMB-002', driver: 'Sarah Wilson' },
	},
	{
		id: 'AC007',
		date: '2023-04-20',
		time: '10:15 AM',
		patient: { name: 'Maria Rodriguez', phone: '+1 (555) 567-8901' },
		location: '159 Birch St, Elsewhere',
		reason: 'Pregnancy Complications',
		status: 'Completed',
		ambulance: { id: 'AMB-003', driver: 'Robert Davis' },
	},
])

// Computed properties
const filteredCalls = computed(() => {
	let filtered = calls.value

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(call) =>
				call.id.toLowerCase().includes(query) ||
				call.patient.name.toLowerCase().includes(query) ||
				call.location.toLowerCase().includes(query) ||
				call.reason.toLowerCase().includes(query),
		)
	}

	// Filter by status
	if (statusFilter.value) {
		filtered = filtered.filter((call) => call.status === statusFilter.value)
	}

	// Filter by active tab
	if (activeTab.value !== 'all') {
		const tabStatusMap = {
			pending: 'Pending',
			'in-progress': 'In Progress',
			completed: 'Completed',
		}
		filtered = filtered.filter((call) => call.status === tabStatusMap[activeTab.value])
	}

	return filtered
})

// Methods
const getStatusBadgeClass = (status) => {
	const classes = {
		Completed: 'bg-green-100 text-green-800',
		'In Progress': 'bg-blue-100 text-blue-800',
		Pending: 'bg-yellow-100 text-yellow-800',
	}
	return classes[status] || 'bg-gray-100 text-gray-800'
}
</script>

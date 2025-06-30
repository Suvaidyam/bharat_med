<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6">
			<h1 class="text-2xl font-bold text-gray-900 mb-4 sm:mb-0">Alloted Rooms</h1>
			<button
				class="bg-black text-white px-4 py-2 rounded-sm hover:bg-gray-800 transition-colors"
			>
				New Allotment
			</button>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
			<div class="bg-white p-6 rounded-sm shadow-sm border">
				<h3 class="text-sm font-medium text-gray-500 mb-2">Total Rooms</h3>
				<p class="text-3xl font-bold text-gray-900">{{ stats.totalRooms }}</p>
			</div>
			<div class="bg-white p-6 rounded-sm shadow-sm border">
				<h3 class="text-sm font-medium text-gray-500 mb-2">Occupied</h3>
				<p class="text-3xl font-bold text-gray-900">{{ stats.occupied }}</p>
			</div>
			<div class="bg-white p-6 rounded-sm shadow-sm border">
				<h3 class="text-sm font-medium text-gray-500 mb-2">Available</h3>
				<p class="text-3xl font-bold text-gray-900">{{ stats.available }}</p>
			</div>
			<div class="bg-white p-6 rounded-sm shadow-sm border">
				<h3 class="text-sm font-medium text-gray-500 mb-2">Occupancy Rate</h3>
				<p class="text-3xl font-bold text-gray-900">{{ stats.occupancyRate }}%</p>
			</div>
		</div>

		<!-- Filters and Search -->
		<div class="bg-white rounded-sm shadow-sm border mb-6">
			<div class="p-4 border-b border-gray-200">
				<div class="flex flex-col lg:flex-row gap-4">
					<!-- Search -->
					<div class="flex-1 relative">
						<svg
							class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400"
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
						<input
							v-model="searchQuery"
							type="text"
							placeholder="Search by patient, room..."
							class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						/>
					</div>

					<!-- Date Range -->
					<div class="flex items-center gap-2">
						<svg
							class="h-4 w-4 text-gray-400"
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
						<span class="text-sm text-gray-600">{{ dateRange }}</span>
					</div>
				</div>
			</div>

			<!-- Filter Row -->
			<div class="p-4 flex flex-wrap gap-4">
				<div class="flex items-center gap-2">
					<span class="text-sm text-gray-600">Filter by:</span>
				</div>

				<select
					v-model="statusFilter"
					class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
				>
					<option value="">All Statuses</option>
					<option value="Occupied">Occupied</option>
					<option value="Discharged">Discharged</option>
				</select>

				<select
					v-model="departmentFilter"
					class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
				>
					<option value="">All Departments</option>
					<option value="Cardiology">Cardiology</option>
					<option value="Orthopedics">Orthopedics</option>
					<option value="Neurology">Neurology</option>
					<option value="Pulmonology">Pulmonology</option>
					<option value="Gastroenterology">Gastroenterology</option>
				</select>

				<select
					v-model="typeFilter"
					class="border border-gray-300 rounded-sm px-3 py-1 text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
				>
					<option value="">All Types</option>
					<option value="Private">Private</option>
					<option value="Semi-Private">Semi-Private</option>
					<option value="General">General</option>
					<option value="ICU">ICU</option>
				</select>
			</div>
		</div>

		<!-- Table -->
		<div class="bg-white rounded-lg shadow-sm border overflow-hidden">
			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="min-w-full divide-y divide-gray-200">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Allotment ID
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Patient
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Room
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Department
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Allotment Date
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Doctor
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
							v-for="allotment in filteredAllotments"
							:key="allotment.id"
							class="hover:bg-gray-50"
						>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								{{ allotment.id }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div>
									<div class="text-sm font-medium text-gray-900">
										{{ allotment.patient.name }}
									</div>
									<div class="text-sm text-gray-500">
										{{ allotment.patient.id }}
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div>
									<div class="text-sm font-medium text-gray-900">
										{{ allotment.room.number }}
									</div>
									<div class="text-sm text-gray-500">
										{{ allotment.room.type }}
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									class="text-sm text-blue-600 hover:text-blue-800 cursor-pointer"
								>
									{{ allotment.department }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								<div class="flex items-center">
									<svg
										class="h-4 w-4 text-gray-400 mr-2"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 002 2z"
										></path>
									</svg>
									{{ formatDate(allotment.allotmentDate) }}
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusClass(allotment.status)"
									class="px-2 py-1 text-xs font-medium rounded-full"
								>
									{{ allotment.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ allotment.doctor }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
								<button class="hover:text-gray-600">
									<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
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

			<!-- Mobile Cards -->
			<div class="lg:hidden">
				<div
					v-for="allotment in filteredAllotments"
					:key="allotment.id"
					class="p-4 border-b border-gray-200 last:border-b-0"
				>
					<div class="flex justify-between items-start mb-2">
						<div>
							<h3 class="text-sm font-medium text-gray-900">
								{{ allotment.patient.name }}
							</h3>
							<p class="text-xs text-gray-500">{{ allotment.patient.id }}</p>
						</div>
						<span
							:class="getStatusClass(allotment.status)"
							class="px-2 py-1 text-xs font-medium rounded-full"
						>
							{{ allotment.status }}
						</span>
					</div>

					<div class="grid grid-cols-2 gap-4 text-sm">
						<div>
							<p class="text-gray-500">Room</p>
							<p class="font-medium">
								{{ allotment.room.number }} ({{ allotment.room.type }})
							</p>
						</div>
						<div>
							<p class="text-gray-500">Department</p>
							<p class="text-blue-600">{{ allotment.department }}</p>
						</div>
						<div>
							<p class="text-gray-500">Doctor</p>
							<p class="font-medium">{{ allotment.doctor }}</p>
						</div>
						<div>
							<p class="text-gray-500">Date</p>
							<p class="font-medium">{{ formatDate(allotment.allotmentDate) }}</p>
						</div>
					</div>

					<div class="flex justify-between items-center mt-3">
						<span class="text-xs text-gray-500">{{ allotment.id }}</span>
						<button class="text-gray-400 hover:text-gray-600">
							<svg class="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
								<path
									d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
								></path>
							</svg>
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
const statusFilter = ref('')
const departmentFilter = ref('')
const typeFilter = ref('')
const dateRange = ref('Jun 30, 2025 - Jun 30, 2025')

// Stats data
const stats = ref({
	totalRooms: 120,
	occupied: 78,
	available: 42,
	occupancyRate: 65,
})

// Sample allotments data
const allotments = ref([
	{
		id: 'RA-001',
		patient: { name: 'John Smith', id: 'P-1001' },
		room: { number: '301', type: 'Private' },
		department: 'Cardiology',
		allotmentDate: '2023-04-15',
		status: 'Occupied',
		doctor: 'Dr. Emily Chen',
	},
	{
		id: 'RA-002',
		patient: { name: 'Sarah Johnson', id: 'P-1002' },
		room: { number: '205', type: 'Semi-Private' },
		department: 'Orthopedics',
		allotmentDate: '2023-04-16',
		status: 'Occupied',
		doctor: 'Dr. Michael Brown',
	},
	{
		id: 'RA-003',
		patient: { name: 'Robert Davis', id: 'P-1003' },
		room: { number: '102', type: 'General' },
		department: 'Neurology',
		allotmentDate: '2023-04-10',
		status: 'Discharged',
		doctor: 'Dr. Lisa Wong',
	},
	{
		id: 'RA-004',
		patient: { name: 'Maria Garcia', id: 'P-1004' },
		room: { number: '405', type: 'ICU' },
		department: 'Pulmonology',
		allotmentDate: '2023-04-17',
		status: 'Occupied',
		doctor: 'Dr. James Wilson',
	},
	{
		id: 'RA-005',
		patient: { name: 'David Lee', id: 'P-1005' },
		room: { number: '210', type: 'Semi-Private' },
		department: 'Gastroenterology',
		allotmentDate: '2023-04-12',
		status: 'Discharged',
		doctor: 'Dr. Sarah Miller',
	},
])

// Computed properties
const filteredAllotments = computed(() => {
	return allotments.value.filter((allotment) => {
		const matchesSearch =
			!searchQuery.value ||
			allotment.patient.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			allotment.patient.id.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			allotment.room.number.toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesStatus = !statusFilter.value || allotment.status === statusFilter.value
		const matchesDepartment =
			!departmentFilter.value || allotment.department === departmentFilter.value
		const matchesType = !typeFilter.value || allotment.room.type === typeFilter.value

		return matchesSearch && matchesStatus && matchesDepartment && matchesType
	})
})

// Methods
const formatDate = (dateString) => {
	const date = new Date(dateString)
	return date.toLocaleDateString('en-US', {
		year: 'numeric',
		month: '2-digit',
		day: '2-digit',
	})
}

const getStatusClass = (status) => {
	switch (status) {
		case 'Occupied':
			return 'bg-gray-900 text-white'
		case 'Discharged':
			return 'bg-gray-100 text-gray-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>

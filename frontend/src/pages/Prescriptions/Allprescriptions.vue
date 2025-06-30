<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header Section -->
		<div class="mb-6">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-2">
				<div>
					<h1 class="text-2xl font-bold text-gray-900 mb-1">Prescriptions</h1>
					<p class="text-gray-600 text-sm">
						Manage patient prescriptions and medications.
					</p>
				</div>
				<button
					class="mt-4 sm:mt-0 bg-black text-white px-4 py-2 rounded-sm hover:bg-gray-800 transition-colors flex items-center gap-2"
				>
					<span class="text-lg">+</span>
					Create Prescription
				</button>
			</div>
		</div>

		<!-- All Prescriptions Section -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<!-- Section Header -->
			<div class="px-6 py-4 border-b border-gray-200">
				<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
					<div>
						<h2 class="text-lg font-semibold text-gray-900 mb-1">All Prescriptions</h2>
						<p class="text-gray-600 text-sm">
							View and manage all patient prescriptions.
						</p>
					</div>
					<div class="flex flex-col sm:flex-row gap-3 mt-4 sm:mt-0">
						<!-- Search Bar -->
						<div class="relative">
							<div
								class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none"
							>
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
										d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
									></path>
								</svg>
							</div>
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search prescriptions..."
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm w-full sm:w-64"
							/>
						</div>
						<!-- Filter Dropdown -->
						<div class="relative">
							<button
								@click="showFilters = !showFilters"
								class="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-sm hover:bg-gray-50 transition-colors text-sm"
							>
								<svg
									class="h-4 w-4"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
									></path>
								</svg>
								All Status
							</button>
						</div>
						<!-- Download Button -->
						<button
							class="flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-sm hover:bg-gray-50 transition-colors text-sm"
						>
							<svg
								class="h-4 w-4"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								></path>
							</svg>
						</button>
					</div>
				</div>
			</div>

			<!-- Table -->
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Patient
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Doctor
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Date
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Medications
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Refills
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
							v-for="prescription in filteredPrescriptions"
							:key="prescription.id"
							class="hover:bg-gray-50"
						>
							<!-- Patient -->
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div
										class="h-10 w-10 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white font-semibold text-sm"
									>
										{{ getInitials(prescription.patient) }}
									</div>
									<div class="ml-3">
										<div class="text-sm font-medium text-gray-900">
											{{ prescription.patient }}
										</div>
									</div>
								</div>
							</td>

							<!-- Doctor -->
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ prescription.doctor }}</div>
							</td>

							<!-- Date -->
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ prescription.date }}</div>
							</td>

							<!-- Status -->
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusClass(prescription.status)"
									class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
								>
									{{ prescription.status }}
								</span>
							</td>

							<!-- Medications -->
							<td class="px-6 py-4">
								<div class="text-sm text-gray-900 space-y-1">
									<div
										v-for="medication in prescription.medications"
										:key="medication"
										class="truncate max-w-xs"
									>
										{{ medication }}
									</div>
								</div>
							</td>

							<!-- Refills -->
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900 text-center">
									{{ prescription.refills }}
								</div>
							</td>

							<!-- Actions -->
							<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
								<button
									class="text-gray-400 hover:text-gray-600 transition-colors"
								>
									<svg
										class="h-5 w-5"
										fill="none"
										stroke="currentColor"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
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
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchQuery = ref('')
const showFilters = ref(false)

// Sample prescription data
const prescriptions = ref([
	{
		id: 1,
		patient: 'John Smith',
		doctor: 'Dr. Sarah Johnson',
		date: '2023-07-15',
		status: 'Active',
		medications: ['Lisinopril 10mg (Once daily)', 'Metformin 500mg (Twice daily)'],
		refills: 2,
	},
	{
		id: 2,
		patient: 'Emily Davis',
		doctor: 'Dr. Michael Chen',
		date: '2023-07-10',
		status: 'Active',
		medications: ['Atorvastatin 20mg (Once daily)'],
		refills: 3,
	},
	{
		id: 3,
		patient: 'Robert Wilson',
		doctor: 'Dr. Lisa Patel',
		date: '2023-06-28',
		status: 'Expired',
		medications: ['Prednisolone 5mg (Once daily)', 'Albuterol 90mcg (As needed)'],
		refills: 0,
	},
	{
		id: 4,
		patient: 'Jessica Brown',
		doctor: 'Dr. James Wilson',
		date: '2023-07-05',
		status: 'Active',
		medications: ['Amoxicillin 500mg (Three times daily)'],
		refills: 0,
	},
	{
		id: 5,
		patient: 'Michael Johnson',
		doctor: 'Dr. Emily Rodriguez',
		date: '2023-07-12',
		status: 'Active',
		medications: ['Sertraline 50mg (Once daily)'],
		refills: 5,
	},
	{
		id: 6,
		patient: 'Sarah Thompson',
		doctor: 'Dr. Robert Kim',
		date: '2023-06-20',
		status: 'Expired',
		medications: ['Hydrochlorothiazide 25mg (Once daily)', 'Ibuprofen 600mg (As needed)'],
		refills: 0,
	},
])

// Computed properties
const filteredPrescriptions = computed(() => {
	return prescriptions.value.filter((prescription) => {
		const searchTerm = searchQuery.value.toLowerCase()
		return (
			prescription.patient.toLowerCase().includes(searchTerm) ||
			prescription.doctor.toLowerCase().includes(searchTerm) ||
			prescription.medications.some((med) => med.toLowerCase().includes(searchTerm))
		)
	})
})

// Helper functions
const getInitials = (name) => {
	return name
		.split(' ')
		.map((word) => word[0])
		.join('')
		.toUpperCase()
}

const getStatusClass = (status) => {
	switch (status.toLowerCase()) {
		case 'active':
			return 'bg-green-100 text-green-800'
		case 'expired':
			return 'bg-red-100 text-red-800'
		case 'pending':
			return 'bg-yellow-100 text-yellow-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>

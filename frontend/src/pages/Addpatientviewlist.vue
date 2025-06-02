<template>
	<div class="min-h-screen bg-gray-50 p-4 sm:p-6 lg:p-8">
		<!-- Header Section -->
		<div class="mb-8">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div>
					<h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Patients</h1>
					<p class="text-gray-600 mt-1">
						Manage your patients and their medical records.
					</p>
				</div>
				<router-link to="/addpatient" class="flex-shrink-0">
					<button
						class="inline-flex items-center px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors duration-200 font-medium"
					>
						<svg
							class="w-5 h-5 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							></path>
						</svg>
						Add Patient
					</button>
				</router-link>
			</div>
		</div>

		<!-- Patients List Section -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<div class="px-4 sm:px-6 py-4 border-b border-gray-200">
				<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
					<div>
						<h2 class="text-lg font-semibold text-gray-900">Patients List</h2>
						<p class="text-sm text-gray-600 mt-1">
							A list of all patients in your clinic with their details.
						</p>
					</div>
					<div class="flex flex-col sm:flex-row gap-3">
						<!-- Search Bar -->
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
								></path>
							</svg>
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search patients..."
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
							/>
						</div>
						<!-- Filters Button -->
						<button
							class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200"
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
									d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
								></path>
							</svg>
							Filters
						</button>
						<!-- Export Button -->
						<button
							class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200"
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
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								></path>
							</svg>
						</button>
					</div>
				</div>
			</div>

			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Name
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Age/Gender
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Last Visit
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Condition
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
							v-for="patient in filteredPatients"
							:key="patient.id"
							class="hover:bg-gray-50 transition-colors duration-150"
						>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<img
										:src="patient.avatar"
										:alt="patient.name"
										class="w-10 h-10 rounded-full mr-3"
									/>
									<div class="text-sm font-medium text-gray-900">
										{{ patient.name }}
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.age }} • {{ patient.gender }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusBadgeClass(patient.status)"
									class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
								>
									{{ patient.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.lastVisit }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.condition }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.doctor }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								<button
									class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
								>
									<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
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
					v-for="patient in filteredPatients"
					:key="patient.id"
					class="p-4 border-b border-gray-200 last:border-b-0"
				>
					<div class="flex items-start space-x-3">
						<img
							:src="patient.avatar"
							:alt="patient.name"
							class="w-12 h-12 rounded-full flex-shrink-0"
						/>
						<div class="flex-1 min-w-0">
							<div class="flex items-center justify-between">
								<h3 class="text-sm font-medium text-gray-900 truncate">
									{{ patient.name }}
								</h3>
								<span
									:class="getStatusBadgeClass(patient.status)"
									class="inline-flex px-2 py-1 text-xs font-semibold rounded-full ml-2"
								>
									{{ patient.status }}
								</span>
							</div>
							<p class="text-sm text-gray-500 mt-1">
								{{ patient.age }} • {{ patient.gender }}
							</p>
							<div class="mt-2 grid grid-cols-1 gap-1 text-xs text-gray-500">
								<div>
									<span class="font-medium">Condition:</span>
									{{ patient.condition }}
								</div>
								<div>
									<span class="font-medium">Doctor:</span> {{ patient.doctor }}
								</div>
								<div>
									<span class="font-medium">Last Visit:</span>
									{{ patient.lastVisit }}
								</div>
							</div>
						</div>
						<button
							class="text-gray-400 hover:text-gray-600 transition-colors duration-200 p-1"
						>
							<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
								<path
									d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
								></path>
							</svg>
						</button>
					</div>
				</div>
			</div>
		</div>

		<!-- Add Patient Modal -->
		<div
			v-if="showAddPatientModal"
			class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
		>
			<div class="bg-white rounded-lg shadow-xl max-w-md w-full">
				<div class="px-6 py-4 border-b border-gray-200">
					<h3 class="text-lg font-semibold text-gray-900">Add New Patient</h3>
				</div>
				<div class="p-6">
					<p class="text-gray-600 mb-4">
						Patient management functionality would be implemented here.
					</p>
					<div class="flex justify-end space-x-3">
						<button
							@click="showAddPatientModal = false"
							class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200"
						>
							Cancel
						</button>
						<button
							@click="showAddPatientModal = false"
							class="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors duration-200"
						>
							Add Patient
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
	name: 'PatientDashboard',
	setup() {
		const searchQuery = ref('')
		const showAddPatientModal = ref(false)

		const patients = ref([
			{
				id: 1,
				name: 'John Smith',
				age: 45,
				gender: 'Male',
				status: 'Active',
				lastVisit: '2023-06-15',
				condition: 'Hypertension',
				doctor: 'Dr. Sarah Johnson',
				avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 2,
				name: 'Emily Davis',
				age: 32,
				gender: 'Female',
				status: 'Active',
				lastVisit: '2023-07-02',
				condition: 'Diabetes Type 2',
				doctor: 'Dr. Michael Chen',
				avatar: 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 3,
				name: 'Robert Wilson',
				age: 58,
				gender: 'Male',
				status: 'Inactive',
				lastVisit: '2023-05-20',
				condition: 'Arthritis',
				doctor: 'Dr. Lisa Patel',
				avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 4,
				name: 'Jessica Brown',
				age: 27,
				gender: 'Female',
				status: 'Active',
				lastVisit: '2023-07-10',
				condition: 'Asthma',
				doctor: 'Dr. James Wilson',
				avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 5,
				name: 'Michael Johnson',
				age: 41,
				gender: 'Male',
				status: 'Active',
				lastVisit: '2023-06-28',
				condition: 'Migraine',
				doctor: 'Dr. Emily Rodriguez',
				avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 6,
				name: 'Sarah Thompson',
				age: 63,
				gender: 'Female',
				status: 'Active',
				lastVisit: '2023-07-05',
				condition: 'Osteoporosis',
				doctor: 'Dr. Robert Kim',
				avatar: 'https://images.unsplash.com/photo-1551836022-deb4988cc6c0?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 7,
				name: 'David Lee',
				age: 52,
				gender: 'Male',
				status: 'Inactive',
				lastVisit: '2023-04-18',
				condition: 'COPD',
				doctor: 'Dr. Jennifer Martinez',
				avatar: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?w=150&h=150&fit=crop&crop=face',
			},
			{
				id: 8,
				name: 'Amanda Clark',
				age: 36,
				gender: 'Female',
				status: 'Active',
				lastVisit: '2023-07-08',
				condition: 'Anxiety',
				doctor: 'Dr. Thomas Wright',
				avatar: 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=150&h=150&fit=crop&crop=face',
			},
		])

		const filteredPatients = computed(() => {
			if (!searchQuery.value) {
				return patients.value
			}

			const query = searchQuery.value.toLowerCase()
			return patients.value.filter(
				(patient) =>
					patient.name.toLowerCase().includes(query) ||
					patient.condition.toLowerCase().includes(query) ||
					patient.doctor.toLowerCase().includes(query),
			)
		})

		const getStatusBadgeClass = (status) => {
			return status === 'Active'
				? 'bg-green-100 text-green-800'
				: 'bg-yellow-100 text-yellow-800'
		}

		return {
			searchQuery,
			showAddPatientModal,
			patients,
			filteredPatients,
			getStatusBadgeClass,
		}
	},
}
</script>

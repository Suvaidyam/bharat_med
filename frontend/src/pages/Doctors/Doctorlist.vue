<template>
	<div class="min-h-screen bg-white p-4 lg:p-6">
		<div class="">
			<!-- Header -->
			<div
				class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8"
			>
				<div>
					<h1 class="text-3xl font-bold text-gray-900">Doctors</h1>
					<p class="text-gray-600 mt-1">
						Manage your medical staff and their information.
					</p>
				</div>
				<button
					@click="addDoctor"
					class="bg-gray-900 hover:bg-gray-800 text-white px-4 py-2 rounded-sm flex items-center gap-2 transition-colors"
				>
					<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M12 4v16m8-8H4"
						/>
					</svg>
					Add Doctor
				</button>
			</div>

			<!-- Doctors List Section -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
				<!-- Section Header -->
				<div class="px-6 py-4 border-b border-gray-200">
					<div
						class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4"
					>
						<div>
							<h2 class="text-xl font-semibold text-gray-900">Doctors List</h2>
							<p class="text-gray-600 text-sm mt-1">
								A list of all doctors in your clinic with their details.
							</p>
						</div>
						<div class="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
							<div class="relative">
								<svg
									class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="m21 21-6-6m2-5a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"
									/>
								</svg>
								<input
									v-model="searchTerm"
									type="text"
									placeholder="Search doctors..."
									class="pl-10 pr-4 py-2 border border-gray-300 rounded-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
								/>
							</div>
							<div class="flex gap-2">
								<button
									class="p-2 border border-gray-300 rounded-sm hover:bg-gray-50 transition-colors"
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
											d="M3 4a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v2.586a1 1 0 0 1-.293.707l-6.414 6.414a1 1 0 0 0-.293.707V17l-4 4v-6.586a1 1 0 0 0-.293-.707L3.293 7.293A1 1 0 0 1 3 6.586V4Z"
										/>
									</svg>
								</button>
								<button
									class="p-2 border border-gray-300 rounded-sm hover:bg-gray-50 transition-colors"
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
											d="M12 10v6m0 0-3-3m3 3 3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
										/>
									</svg>
								</button>
							</div>
						</div>
					</div>
				</div>

				<!-- Desktop Table View -->
				<div class="hidden lg:block overflow-x-auto">
					<table class="w-full">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Name
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Specialty
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Patients
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Experience
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Contact
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
								v-for="doctor in filteredDoctors"
								:key="doctor.id"
								class="hover:bg-gray-50 transition-colors"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="flex items-center">
										<div
											:class="getAvatarClass(doctor.name)"
											class="w-10 h-10 rounded-full flex items-center justify-center text-white font-medium text-sm"
										>
											{{ getInitials(doctor.name) }}
										</div>
										<div class="ml-3">
											<div class="text-sm font-medium text-gray-900">
												{{ doctor.name }}
											</div>
										</div>
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									{{ doctor.specialty }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getStatusClass(doctor.status)"
										class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
									>
										{{ doctor.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									{{ doctor.patients }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									{{ doctor.experience }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									<div>{{ doctor.email }}</div>
									<div class="text-gray-500">{{ doctor.phone }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
									<button
										@click="showActions(doctor.id)"
										class="p-1 hover:bg-gray-100 rounded transition-colors"
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
												d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
											/>
										</svg>
									</button>
								</td>
							</tr>
						</tbody>
					</table>
				</div>

				<!-- Mobile Card View -->
				<div class="lg:hidden divide-y divide-gray-200">
					<div v-for="doctor in filteredDoctors" :key="doctor.id" class="p-4">
						<div class="flex items-start justify-between">
							<div class="flex items-center flex-1">
								<div
									:class="getAvatarClass(doctor.name)"
									class="w-10 h-10 rounded-full flex items-center justify-center text-white font-medium text-sm"
								>
									{{ getInitials(doctor.name) }}
								</div>
								<div class="ml-3 flex-1">
									<div class="flex items-center justify-between">
										<h3 class="text-sm font-medium text-gray-900">
											{{ doctor.name }}
										</h3>
										<button
											@click="showActions(doctor.id)"
											class="p-1 hover:bg-gray-100 rounded transition-colors"
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
													d="M12 5v.01M12 12v.01M12 19v.01M12 6a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2zm0 7a1 1 0 110-2 1 1 0 010 2z"
												/>
											</svg>
										</button>
									</div>
									<p class="text-sm text-gray-600">{{ doctor.specialty }}</p>
									<div class="mt-2 flex items-center gap-2 flex-wrap">
										<span
											:class="getStatusClass(doctor.status)"
											class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
										>
											{{ doctor.status }}
										</span>
										<span class="text-xs text-gray-500"
											>{{ doctor.patients }} patients</span
										>
										<span class="text-xs text-gray-500">{{
											doctor.experience
										}}</span>
									</div>
									<div class="mt-2 text-xs text-gray-600">
										<div>{{ doctor.email }}</div>
										<div>{{ doctor.phone }}</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchTerm = ref('')

const doctors = ref([
	{
		id: 1,
		name: 'Dr. Sarah Johnson',
		specialty: 'Cardiology',
		status: 'Active',
		patients: 120,
		experience: '8 years',
		email: 'sarah.johnson@medixpro.com',
		phone: '+1 (555) 123-4567',
	},
	{
		id: 2,
		name: 'Dr. Michael Chen',
		specialty: 'Neurology',
		status: 'Active',
		patients: 85,
		experience: '12 years',
		email: 'michael.chen@medixpro.com',
		phone: '+1 (555) 234-5678',
	},
	{
		id: 3,
		name: 'Dr. Lisa Patel',
		specialty: 'Pediatrics',
		status: 'On Leave',
		patients: 150,
		experience: '10 years',
		email: 'lisa.patel@medixpro.com',
		phone: '+1 (555) 345-6789',
	},
	{
		id: 4,
		name: 'Dr. James Wilson',
		specialty: 'Orthopedics',
		status: 'Active',
		patients: 95,
		experience: '15 years',
		email: 'james.wilson@medixpro.com',
		phone: '+1 (555) 456-7890',
	},
	{
		id: 5,
		name: 'Dr. Emily Rodriguez',
		specialty: 'Dermatology',
		status: 'Active',
		patients: 110,
		experience: '7 years',
		email: 'emily.rodriguez@medixpro.com',
		phone: '+1 (555) 567-8901',
	},
	{
		id: 6,
		name: 'Dr. Robert Kim',
		specialty: 'Psychiatry',
		status: 'Inactive',
		patients: 75,
		experience: '9 years',
		email: 'robert.kim@medixpro.com',
		phone: '+1 (555) 678-9012',
	},
])

// Computed properties
const filteredDoctors = computed(() => {
	return doctors.value.filter(
		(doctor) =>
			doctor.name.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
			doctor.specialty.toLowerCase().includes(searchTerm.value.toLowerCase()),
	)
})

// Methods
const getStatusClass = (status) => {
	switch (status) {
		case 'Active':
			return 'bg-green-100 text-green-800'
		case 'On Leave':
			return 'bg-yellow-100 text-yellow-800'
		case 'Inactive':
			return 'bg-red-100 text-red-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

const getInitials = (name) => {
	return name
		.split(' ')
		.map((n) => n[0])
		.join('')
}

const getAvatarClass = (name) => {
	const colors = [
		'bg-blue-500',
		'bg-green-500',
		'bg-purple-500',
		'bg-pink-500',
		'bg-indigo-500',
		'bg-yellow-500',
	]
	const colorIndex = name.length % colors.length
	return colors[colorIndex]
}

const addDoctor = () => {
	console.log('Add doctor clicked')
	// Add your logic here
}

const showActions = (doctorId) => {
	console.log('Actions for doctor:', doctorId)
	// Add your actions logic here
}
</script>

<style scoped>
/* Additional custom styles if needed */
</style>

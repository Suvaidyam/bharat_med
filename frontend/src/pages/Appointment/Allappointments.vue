<template>
	<div class="min-h-screen bg-white p-4 md:p-6">
		<div class="">
			<!-- Header -->
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-6">
				<div>
					<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">Appointments</h1>
					<p class="text-gray-600">Manage your clinic's appointments and schedules.</p>
				</div>
				<div class="flex flex-col sm:flex-row gap-3 mt-4 sm:mt-0">
					<button
						class="inline-flex items-center px-4 py-2 border border-gray-300 rounded-sm shadow-sm bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
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
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							></path>
						</svg>
						Calendar View
					</button>
					<button
						class="inline-flex items-center px-4 py-2 bg-gray-900 text-white text-sm font-medium rounded-sm hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900"
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
							></path>
						</svg>
						New Appointment
					</button>
				</div>
			</div>

			<!-- Tabs -->
			<div class="border-b border-gray-200 mb-6">
				<nav class="-mb-px flex space-x-8 overflow-x-auto">
					<button
						v-for="tab in tabs"
						:key="tab.id"
						@click="activeTab = tab.id"
						:class="[
							'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm',
							activeTab === tab.id
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
						]"
					>
						{{ tab.name }}
					</button>
				</nav>
			</div>

			<!-- Content Section -->
			<div class="bg-white rounded-lg shadow">
				<!-- Section Header -->
				<div class="px-4 py-5 sm:px-6 border-b border-gray-200">
					<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
						<div>
							<h3 class="text-lg leading-6 font-medium text-gray-900">
								All Appointments
							</h3>
							<p class="mt-1 max-w-2xl text-sm text-gray-500">
								View and manage all scheduled appointments.
							</p>
						</div>
						<div class="mt-4 sm:mt-0 flex flex-col sm:flex-row gap-3">
							<div class="relative">
								<input
									v-model="searchQuery"
									type="text"
									placeholder="Search appointments..."
									class="w-full sm:w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
								/>
								<svg
									class="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
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
							<button
								class="inline-flex items-center px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-700 bg-white hover:bg-gray-50"
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
								Filter
							</button>
							<button
								class="inline-flex items-center px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-700 bg-white hover:bg-gray-50"
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
								Export
							</button>
						</div>
					</div>
				</div>

				<!-- Desktop Table -->
				<div class="hidden lg:block overflow-hidden">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
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
									Date & Time
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Status
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
									Actions
								</th>
							</tr>
						</thead>
						<tbody class="bg-white divide-y divide-gray-200">
							<tr
								v-for="appointment in filteredAppointments"
								:key="appointment.id"
								class="hover:bg-gray-50"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="flex items-center">
										<div class="flex-shrink-0 h-10 w-10">
											<img
												class="h-10 w-10 rounded-full"
												:src="appointment.patient.avatar"
												:alt="appointment.patient.name"
											/>
										</div>
										<div class="ml-4">
											<div class="text-sm font-medium text-gray-900">
												{{ appointment.patient.name }}
											</div>
										</div>
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									{{ appointment.doctor }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
									<div>{{ appointment.date }}</div>
									<div>{{ appointment.time }}</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<span
										:class="getStatusClass(appointment.status)"
										class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
									>
										{{ appointment.status }}
									</span>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
									{{ appointment.type }}
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
									{{ appointment.duration }}
								</td>
								<td
									class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
								>
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

				<!-- Mobile Cards -->
				<div class="lg:hidden">
					<div
						v-for="appointment in filteredAppointments"
						:key="appointment.id"
						class="p-4 border-b border-gray-200 last:border-b-0"
					>
						<div class="flex items-center justify-between mb-3">
							<div class="flex items-center">
								<img
									class="h-10 w-10 rounded-full"
									:src="appointment.patient.avatar"
									:alt="appointment.patient.name"
								/>
								<div class="ml-3">
									<p class="text-sm font-medium text-gray-900">
										{{ appointment.patient.name }}
									</p>
									<p class="text-sm text-gray-500">{{ appointment.doctor }}</p>
								</div>
							</div>
							<button class="text-gray-400 hover:text-gray-600">
								<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
									<path
										d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
									></path>
								</svg>
							</button>
						</div>
						<div class="grid grid-cols-2 gap-4 text-sm">
							<div>
								<p class="text-gray-500">Date & Time</p>
								<p class="text-gray-900">
									{{ appointment.date }} {{ appointment.time }}
								</p>
							</div>
							<div>
								<p class="text-gray-500">Type</p>
								<p class="text-gray-900">{{ appointment.type }}</p>
							</div>
							<div>
								<p class="text-gray-500">Duration</p>
								<p class="text-gray-900">{{ appointment.duration }}</p>
							</div>
							<div>
								<p class="text-gray-500">Status</p>
								<span
									:class="getStatusClass(appointment.status)"
									class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
								>
									{{ appointment.status }}
								</span>
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

const activeTab = ref('all')
const searchQuery = ref('')

const tabs = [
	{ id: 'all', name: 'All Appointments' },
	{ id: 'upcoming', name: 'Upcoming' },
	{ id: 'today', name: 'Today' },
	{ id: 'completed', name: 'Completed' },
	{ id: 'cancelled', name: 'Cancelled' },
]

const appointments = ref([
	{
		id: 1,
		patient: {
			name: 'John Smith',
			avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Sarah Johnson',
		date: '2023-07-15',
		time: '10:00 AM',
		status: 'Confirmed',
		type: 'Check-up',
		duration: '30 min',
	},
	{
		id: 2,
		patient: {
			name: 'Emily Davis',
			avatar: 'https://images.unsplash.com/photo-1494790108755-2616c64c29d7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Michael Chen',
		date: '2025-06-09',
		time: '11:30 AM',
		status: 'In Progress',
		type: 'Consultation',
		duration: '45 min',
	},
	{
		id: 3,
		patient: {
			name: 'Robert Wilson',
			avatar: 'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Lisa Patel',
		date: '2025-06-09',
		time: '02:15 PM',
		status: 'Completed',
		type: 'Follow-up',
		duration: '20 min',
	},
	{
		id: 4,
		patient: {
			name: 'Jessica Brown',
			avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. James Wilson',
		date: '2023-07-25',
		time: '09:00 AM',
		status: 'Confirmed',
		type: 'Dental Cleaning',
		duration: '60 min',
	},
	{
		id: 5,
		patient: {
			name: 'Michael Johnson',
			avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Emily Rodriguez',
		date: '2023-07-28',
		time: '10:30 AM',
		status: 'Confirmed',
		type: 'X-Ray',
		duration: '15 min',
	},
	{
		id: 6,
		patient: {
			name: 'Sarah Thompson',
			avatar: 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Robert Kim',
		date: '2023-07-10',
		time: '01:45 PM',
		status: 'Cancelled',
		type: 'Therapy Session',
		duration: '45 min',
	},
	{
		id: 7,
		patient: {
			name: 'David Miller',
			avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Jennifer Lee',
		date: '2023-07-05',
		time: '11:00 AM',
		status: 'Completed',
		type: 'Annual Physical',
		duration: '60 min',
	},
	{
		id: 8,
		patient: {
			name: 'Amanda Clark',
			avatar: 'https://images.unsplash.com/photo-1534751516642-a1af1ef26a56?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
		},
		doctor: 'Dr. Thomas Brown',
		date: '2023-07-08',
		time: '09:30 AM',
		status: 'Cancelled',
		type: 'Vaccination',
		duration: '15 min',
	},
])

const filteredAppointments = computed(() => {
	let filtered = appointments.value

	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(appointment) =>
				appointment.patient.name.toLowerCase().includes(query) ||
				appointment.doctor.toLowerCase().includes(query) ||
				appointment.type.toLowerCase().includes(query),
		)
	}

	if (activeTab.value !== 'all') {
		filtered = filtered.filter((appointment) => {
			switch (activeTab.value) {
				case 'upcoming':
					return appointment.status === 'Confirmed'
				case 'today':
					return appointment.date === '2025-06-09'
				case 'completed':
					return appointment.status === 'Completed'
				case 'cancelled':
					return appointment.status === 'Cancelled'
				default:
					return true
			}
		})
	}

	return filtered
})

const getStatusClass = (status) => {
	switch (status) {
		case 'Confirmed':
			return 'bg-blue-100 text-blue-800'
		case 'In Progress':
			return 'bg-yellow-100 text-yellow-800'
		case 'Completed':
			return 'bg-green-100 text-green-800'
		case 'Cancelled':
			return 'bg-red-100 text-red-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}
</script>

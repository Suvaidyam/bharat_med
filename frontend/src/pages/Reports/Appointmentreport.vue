<template>
	<div class="min-h-screen bg-gray-50 p-4 md:p-6">
		<!-- Header -->
		<div class="mb-6">
			<h1 class="text-2xl font-bold text-gray-900 mb-2">Appointment Reports</h1>
			<p class="text-gray-600">
				Analyze appointment data, track trends, and generate detailed reports
			</p>
		</div>

		<!-- Filters -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200 p-4 mb-6">
			<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
				<div class="flex flex-col sm:flex-row gap-4">
					<!-- Date Range -->
					<div
						class="flex items-center gap-2 px-3 py-2 border border-gray-300 rounded-md"
					>
						<svg
							class="w-4 h-4 text-gray-400"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M8 7V3a1 1 0 011-1h6a1 1 0 011 1v4m-6 0h6M3 21h18a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
						<span class="text-sm text-gray-700">{{ dateRange }}</span>
					</div>

					<!-- Department Filter -->
					<select
						v-model="selectedDepartment"
						class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
					>
						<option value="all">All Departments</option>
						<option value="cardiology">Cardiology</option>
						<option value="neurology">Neurology</option>
						<option value="orthopedics">Orthopedics</option>
						<option value="pediatrics">Pediatrics</option>
						<option value="dermatology">Dermatology</option>
						<option value="general">General Medicine</option>
					</select>

					<!-- Doctor Filter -->
					<select
						v-model="selectedDoctor"
						class="px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
					>
						<option value="all">All Doctors</option>
						<option value="dr-smith">Dr. Smith</option>
						<option value="dr-johnson">Dr. Johnson</option>
						<option value="dr-williams">Dr. Williams</option>
						<option value="dr-brown">Dr. Brown</option>
					</select>
				</div>

				<div class="flex items-center gap-3">
					<button
						class="flex items-center gap-2 px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
							/>
						</svg>
						Refresh
					</button>
					<button
						class="flex items-center gap-2 px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 10v6m0 0l-3-3m3 3l3-3M3 17V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2z"
							/>
						</svg>
						Export
					</button>
				</div>
			</div>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<div class="text-sm font-medium text-gray-500">Total Appointments</div>
					<div class="w-8 h-8 bg-gray-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-4 h-4 text-gray-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M8 7V3a1 1 0 011-1h6a1 1 0 011 1v4m-6 0h6M3 21h18a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">
					{{ stats.total.toLocaleString() }}
				</div>
				<div class="text-sm text-green-600">+12.5% from last month</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-3">
					<div class="bg-gray-400 h-1 rounded-full" style="width: 100%"></div>
				</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<div class="text-sm font-medium text-gray-500">Completed</div>
					<div class="w-8 h-8 bg-green-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-4 h-4 text-green-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M5 13l4 4L19 7"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">
					{{ stats.completed.toLocaleString() }}
				</div>
				<div class="text-sm text-gray-500">
					{{ stats.completionRate }}% completion rate
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-3">
					<div
						class="bg-green-500 h-1 rounded-full"
						:style="`width: ${stats.completionRate}%`"
					></div>
				</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<div class="text-sm font-medium text-gray-500">Canceled</div>
					<div class="w-8 h-8 bg-red-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-4 h-4 text-red-600"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900 mb-1">
					{{ stats.canceled.toLocaleString() }}
				</div>
				<div class="text-sm text-gray-500">
					{{ stats.cancellationRate }}% cancellation rate
				</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-3">
					<div
						class="bg-red-500 h-1 rounded-full"
						:style="`width: ${stats.cancellationRate}%`"
					></div>
				</div>
			</div>

			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<div class="flex items-center justify-between mb-4">
					<div class="text-sm font-medium text-gray-500">No-Shows</div>
					<div class="w-8 h-8 bg-orange-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-4 h-4 text-orange-600"
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
				<div class="text-3xl font-bold text-gray-900 mb-1">
					{{ stats.noShows.toLocaleString() }}
				</div>
				<div class="text-sm text-gray-500">{{ stats.noShowRate }}% no-show rate</div>
				<div class="w-full bg-gray-200 rounded-full h-1 mt-3">
					<div
						class="bg-orange-500 h-1 rounded-full"
						:style="`width: ${stats.noShowRate}%`"
					></div>
				</div>
			</div>
		</div>

		<!-- Navigation Tabs -->
		<div class="mb-6">
			<div class="flex space-x-8 border-b border-gray-200">
				<button
					v-for="tab in tabs"
					:key="tab.id"
					@click="activeTab = tab.id"
					:class="[
						'py-2 px-1 border-b-2 font-medium text-sm transition-colors',
						activeTab === tab.id
							? 'border-blue-500 text-blue-600'
							: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
					]"
				>
					{{ tab.name }}
				</button>
			</div>
		</div>

		<!-- Charts Section -->
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
			<!-- Pie Chart -->
			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">
					Appointment Status Distribution
				</h3>
				<p class="text-sm text-gray-500 mb-6">
					Breakdown of appointments by their current status
				</p>

				<div class="flex items-center justify-center mb-6">
					<div class="relative">
						<svg class="w-64 h-64 transform -rotate-90" viewBox="0 0 120 120">
							<!-- Completed (70%) -->
							<circle
								cx="60"
								cy="60"
								r="54"
								fill="none"
								stroke="#e5e7eb"
								stroke-width="12"
							/>
							<circle
								cx="60"
								cy="60"
								r="54"
								fill="none"
								stroke="#3b82f6"
								stroke-width="12"
								stroke-dasharray="238"
								stroke-dashoffset="71.4"
								stroke-linecap="round"
							/>
							<!-- Canceled (15%) -->
							<circle
								cx="60"
								cy="60"
								r="54"
								fill="none"
								stroke="#fbbf24"
								stroke-width="12"
								stroke-dasharray="36"
								stroke-dashoffset="202"
								stroke-linecap="round"
							/>
							<!-- No-Show (7%) -->
							<circle
								cx="60"
								cy="60"
								r="54"
								fill="none"
								stroke="#f87171"
								stroke-width="12"
								stroke-dasharray="17"
								stroke-dashoffset="166"
								stroke-linecap="round"
							/>
							<!-- Scheduled (8%) -->
							<circle
								cx="60"
								cy="60"
								r="54"
								fill="none"
								stroke="#10b981"
								stroke-width="12"
								stroke-dasharray="19"
								stroke-dashoffset="149"
								stroke-linecap="round"
							/>
						</svg>
						<div class="absolute inset-0 flex items-center justify-center">
							<div class="text-center">
								<div class="text-2xl font-bold text-gray-900">
									{{ stats.total }}
								</div>
								<div class="text-sm text-gray-500">Total</div>
							</div>
						</div>
					</div>
				</div>

				<div class="grid grid-cols-2 gap-4">
					<div class="flex items-center gap-3">
						<div class="w-3 h-3 bg-blue-500 rounded-full"></div>
						<div>
							<div class="text-sm font-medium text-gray-900">Completed: 70%</div>
						</div>
					</div>
					<div class="flex items-center gap-3">
						<div class="w-3 h-3 bg-green-500 rounded-full"></div>
						<div>
							<div class="text-sm font-medium text-gray-900">Scheduled: 8%</div>
						</div>
					</div>
					<div class="flex items-center gap-3">
						<div class="w-3 h-3 bg-yellow-400 rounded-full"></div>
						<div>
							<div class="text-sm font-medium text-gray-900">Canceled: 15%</div>
						</div>
					</div>
					<div class="flex items-center gap-3">
						<div class="w-3 h-3 bg-red-400 rounded-full"></div>
						<div>
							<div class="text-sm font-medium text-gray-900">No-Show: 7%</div>
						</div>
					</div>
				</div>
			</div>

			<!-- Bar Chart -->
			<div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">
					Appointments by Department
				</h3>
				<p class="text-sm text-gray-500 mb-6">
					Distribution of appointments across different departments
				</p>

				<div class="space-y-4">
					<div
						v-for="dept in departmentData"
						:key="dept.name"
						class="flex items-center gap-4"
					>
						<div class="w-24 text-sm text-gray-600 text-right">{{ dept.name }}</div>
						<div class="flex-1 relative">
							<div class="w-full bg-gray-200 rounded-full h-6">
								<div
									class="bg-indigo-500 h-6 rounded-full flex items-center justify-end pr-2 transition-all duration-500"
									:style="`width: ${(dept.count / 280) * 100}%`"
								>
									<span class="text-xs text-white font-medium">{{
										dept.count
									}}</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<div class="mt-6 flex items-center justify-between text-xs text-gray-500">
					<span>0</span>
					<span>65</span>
					<span>130</span>
					<span>195</span>
					<span>280</span>
				</div>

				<div class="mt-2 flex items-center gap-2">
					<div class="w-3 h-3 bg-indigo-500 rounded-sm"></div>
					<span class="text-sm text-gray-600">Appointments</span>
				</div>
			</div>
		</div>

		<!-- Recent Appointments Table -->
		<div class="bg-white rounded-lg shadow-sm border border-gray-200">
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
					<div>
						<h3 class="text-lg font-semibold text-gray-900">Recent Appointments</h3>
						<p class="text-sm text-gray-500">
							Detailed view of the last 10 appointments
						</p>
					</div>
					<div class="flex items-center gap-3">
						<div class="relative">
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search appointments..."
								class="w-full sm:w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
							<svg
								class="absolute left-3 top-2.5 h-4 w-4 text-gray-400"
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
						</div>
						<button
							class="flex items-center gap-2 px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
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
							Filter
						</button>
					</div>
				</div>
			</div>

			<div class="overflow-x-auto">
				<table class="w-full">
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
								Service
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
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
								<div class="text-sm font-medium text-gray-900">
									{{ appointment.patient }}
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ appointment.doctor }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ appointment.dateTime }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm text-gray-900">{{ appointment.service }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="[
										'inline-flex px-2 py-1 text-xs font-medium rounded-full',
										appointment.status === 'Completed'
											? 'bg-green-100 text-green-800'
											: appointment.status === 'Canceled'
												? 'bg-red-100 text-red-800'
												: appointment.status === 'Scheduled'
													? 'bg-blue-100 text-blue-800'
													: 'bg-orange-100 text-orange-800',
									]"
								>
									{{ appointment.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-right">
								<button class="text-gray-400 hover:text-gray-600">
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

// Active tab
const activeTab = ref('overview')

// Filters
const selectedDepartment = ref('all')
const selectedDoctor = ref('all')
const dateRange = ref('Jul 01, 2025 - Jul 01, 2025')
const searchQuery = ref('')

// Stats data
const stats = ref({
	total: 1248,
	completed: 876,
	canceled: 187,
	noShows: 85,
	completionRate: 70.2,
	cancellationRate: 15,
	noShowRate: 6.8,
})

// Navigation tabs
const tabs = ref([
	{ id: 'overview', name: 'Overview' },
	{ id: 'trends', name: 'Trends' },
	{ id: 'by-doctor', name: 'By Doctor' },
	{ id: 'by-service', name: 'By Service' },
])

// Department data for bar chart
const departmentData = ref([
	{ name: 'Cardiology', count: 280 },
	{ name: 'Neurology', count: 265 },
	{ name: 'Orthopedics', count: 245 },
	{ name: 'Pediatrics', count: 220 },
	{ name: 'Dermatology', count: 185 },
	{ name: 'General Medicine', count: 53 },
])

// Recent appointments data
const appointments = ref([
	{
		id: 1,
		patient: 'Emma Thompson',
		doctor: 'Dr. Smith',
		dateTime: 'Today, 9:30 AM',
		service: 'General Checkup',
		status: 'Completed',
	},
	{
		id: 2,
		patient: 'James Wilson',
		doctor: 'Dr. Johnson',
		dateTime: 'Today, 10:15 AM',
		service: 'Cardiology Consultation',
		status: 'Completed',
	},
	{
		id: 3,
		patient: 'Sarah Davis',
		doctor: 'Dr. Williams',
		dateTime: 'Today, 11:00 AM',
		service: 'Pediatric Checkup',
		status: 'Scheduled',
	},
	{
		id: 4,
		patient: 'Michael Brown',
		doctor: 'Dr. Brown',
		dateTime: 'Today, 2:30 PM',
		service: 'Orthopedic Consultation',
		status: 'Canceled',
	},
	{
		id: 5,
		patient: 'Lisa Anderson',
		doctor: 'Dr. Smith',
		dateTime: 'Today, 3:15 PM',
		service: 'Dermatology Consultation',
		status: 'No-Show',
	},
])

// Computed properties
const filteredAppointments = computed(() => {
	return appointments.value.filter((appointment) => {
		const matchesSearch =
			appointment.patient.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			appointment.doctor.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			appointment.service.toLowerCase().includes(searchQuery.value.toLowerCase())

		return matchesSearch
	})
})
</script>

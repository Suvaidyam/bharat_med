<template>
	<div class="min-h-screen bg-gray-50 p-4 lg:p-6">
		<!-- Header -->
		<div class="mb-8">
			<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between mb-4">
				<div>
					<h1 class="text-2xl lg:text-3xl font-bold text-gray-900 mb-2">
						Patient Visit Report
					</h1>
					<p class="text-gray-600">
						Track patient visits, demographics, and health trends
					</p>
				</div>
				<div class="flex items-center space-x-3 mt-4 lg:mt-0">
					<button
						class="flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
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
							/>
						</svg>
						Export
					</button>
					<button
						class="flex items-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
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
								d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
							/>
						</svg>
						Refresh
					</button>
				</div>
			</div>

			<!-- Date Range and Filters -->
			<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
				<div
					class="flex flex-col sm:flex-row items-start sm:items-center space-y-2 sm:space-y-0 sm:space-x-4"
				>
					<div class="flex items-center space-x-2 bg-white px-4 py-2 rounded-lg border">
						<svg
							class="w-4 h-4 text-gray-500"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							/>
						</svg>
						<span class="text-sm font-medium">Jul 01, 2025 - Jul 01, 2025</span>
					</div>
					<select class="bg-white border border-gray-300 rounded-lg px-4 py-2 text-sm">
						<option>All Departments</option>
					</select>
					<select class="bg-white border border-gray-300 rounded-lg px-4 py-2 text-sm">
						<option>All Doctors</option>
					</select>
				</div>
				<div class="mt-4 lg:mt-0">
					<div class="relative">
						<input
							type="text"
							placeholder="Search patients..."
							class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
						/>
						<svg
							class="w-4 h-4 text-gray-400 absolute left-3 top-3"
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
				</div>
			</div>
		</div>

		<!-- Key Metrics -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6 mb-8">
			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<div class="p-2 bg-blue-100 rounded-lg">
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
								d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
							/>
						</svg>
					</div>
					<span class="text-sm font-medium text-green-600 bg-green-100 px-2 py-1 rounded"
						>+12.5%</span
					>
				</div>
				<h3 class="text-sm font-medium text-gray-500 mb-1">Total Visits</h3>
				<p class="text-3xl font-bold text-gray-900">3,842</p>
				<p class="text-xs text-gray-500 mt-1">from previous period</p>
			</div>

			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<div class="p-2 bg-green-100 rounded-lg">
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
								d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
							/>
						</svg>
					</div>
					<span class="text-sm font-medium text-green-600 bg-green-100 px-2 py-1 rounded"
						>+8.2%</span
					>
				</div>
				<h3 class="text-sm font-medium text-gray-500 mb-1">New Patients</h3>
				<p class="text-3xl font-bold text-gray-900">428</p>
				<p class="text-xs text-gray-500 mt-1">from previous period</p>
			</div>

			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<div class="p-2 bg-orange-100 rounded-lg">
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
					<span class="text-sm font-medium text-red-600 bg-red-100 px-2 py-1 rounded"
						>-2 min</span
					>
				</div>
				<h3 class="text-sm font-medium text-gray-500 mb-1">Avg. Visit Duration</h3>
				<p class="text-3xl font-bold text-gray-900">
					32 <span class="text-lg text-gray-500">min</span>
				</p>
				<p class="text-xs text-gray-500 mt-1">from previous period</p>
			</div>

			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<div class="flex items-center justify-between mb-4">
					<div class="p-2 bg-red-100 rounded-lg">
						<svg
							class="w-6 h-6 text-red-600"
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
					<span class="text-sm font-medium text-green-600 bg-green-100 px-2 py-1 rounded"
						>-0.3%</span
					>
				</div>
				<h3 class="text-sm font-medium text-gray-500 mb-1">No-Show Rate</h3>
				<p class="text-3xl font-bold text-gray-900">
					6.8<span class="text-lg text-gray-500">%</span>
				</p>
				<p class="text-xs text-gray-500 mt-1">from previous period</p>
			</div>
		</div>

		<!-- Navigation Tabs -->
		<div class="mb-6">
			<nav class="flex space-x-8 border-b border-gray-200">
				<button
					v-for="tab in tabs"
					:key="tab.id"
					@click="activeTab = tab.id"
					:class="[
						'py-2 px-1 border-b-2 font-medium text-sm',
						activeTab === tab.id
							? 'border-blue-500 text-blue-600'
							: 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300',
					]"
				>
					{{ tab.name }}
				</button>
			</nav>
		</div>

		<!-- Charts Section -->
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
			<!-- Visit Types Chart -->
			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Visit Types</h3>
				<p class="text-sm text-gray-600 mb-6">Distribution of patient visits by type</p>
				<div class="flex items-center justify-center h-64">
					<div class="relative w-48 h-48">
						<svg class="w-full h-full transform -rotate-90" viewBox="0 0 42 42">
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#e5e7eb"
								stroke-width="3"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#3b82f6"
								stroke-width="3"
								stroke-dasharray="35 65"
								stroke-dashoffset="0"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#10b981"
								stroke-width="3"
								stroke-dasharray="25 75"
								stroke-dashoffset="-35"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#f59e0b"
								stroke-width="3"
								stroke-dasharray="20 80"
								stroke-dashoffset="-60"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#ef4444"
								stroke-width="3"
								stroke-dasharray="20 80"
								stroke-dashoffset="-80"
							/>
						</svg>
					</div>
				</div>
				<div class="grid grid-cols-2 gap-4 mt-4">
					<div class="flex items-center">
						<div class="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Routine (35%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Follow-up (25%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Emergency (20%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Consultation (20%)</span>
					</div>
				</div>
			</div>

			<!-- Visit Outcomes Chart -->
			<div class="bg-white rounded-xl p-6 shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Visit Outcomes</h3>
				<p class="text-sm text-gray-600 mb-6">Outcomes of patient visits</p>
				<div class="flex items-center justify-center h-64">
					<div class="relative w-48 h-48">
						<svg class="w-full h-full transform -rotate-90" viewBox="0 0 42 42">
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#e5e7eb"
								stroke-width="3"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#3b82f6"
								stroke-width="3"
								stroke-dasharray="40 60"
								stroke-dashoffset="0"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#10b981"
								stroke-width="3"
								stroke-dasharray="30 70"
								stroke-dashoffset="-40"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#f59e0b"
								stroke-width="3"
								stroke-dasharray="20 80"
								stroke-dashoffset="-70"
							/>
							<circle
								cx="21"
								cy="21"
								r="15.915"
								fill="transparent"
								stroke="#ef4444"
								stroke-width="3"
								stroke-dasharray="10 90"
								stroke-dashoffset="-90"
							/>
						</svg>
					</div>
				</div>
				<div class="grid grid-cols-2 gap-4 mt-4">
					<div class="flex items-center">
						<div class="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Treated (40%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Referred (30%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-yellow-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Follow-up (20%)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
						<span class="text-sm text-gray-600">Discharged (10%)</span>
					</div>
				</div>
			</div>
		</div>

		<!-- Recent Patient Visits Table -->
		<div class="bg-white rounded-xl shadow-sm border">
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
					<div>
						<h3 class="text-lg font-semibold text-gray-900">Recent Patient Visits</h3>
						<p class="text-sm text-gray-600 mt-1">
							Latest patient visits and their details
						</p>
					</div>
					<button
						class="flex items-center px-4 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 mt-4 sm:mt-0"
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
							/>
						</svg>
						Filter
					</button>
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
								Visit Date
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Department
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Doctor
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Visit Type
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr v-for="patient in patients" :key="patient.id" class="hover:bg-gray-50">
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="text-sm font-medium text-gray-900">
									{{ patient.name }}
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.visitDate }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.department }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.doctor }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
								{{ patient.visitType }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="[
										'inline-flex px-2 py-1 text-xs font-semibold rounded-full',
										patient.status === 'Completed'
											? 'bg-green-100 text-green-800'
											: 'bg-yellow-100 text-yellow-800',
									]"
								>
									{{ patient.status }}
								</span>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('overview')

const tabs = [
	{ id: 'overview', name: 'Overview' },
	{ id: 'demographics', name: 'Demographics' },
	{ id: 'trends', name: 'Visit Trends' },
	{ id: 'conditions', name: 'Conditions' },
]

const patients = [
	{
		id: 1,
		name: 'Sarah Johnson',
		visitDate: 'Apr 19, 2023',
		department: 'Cardiology',
		doctor: 'Dr. Smith',
		visitType: 'Follow-up',
		status: 'Completed',
	},
	{
		id: 2,
		name: 'Michael Brown',
		visitDate: 'Apr 18, 2023',
		department: 'Orthopedics',
		doctor: 'Dr. Williams',
		visitType: 'New Patient',
		status: 'Completed',
	},
	{
		id: 3,
		name: 'Emily Davis',
		visitDate: 'Apr 17, 2023',
		department: 'Pediatrics',
		doctor: 'Dr. Johnson',
		visitType: 'Follow-up',
		status: 'Completed',
	},
]
</script>

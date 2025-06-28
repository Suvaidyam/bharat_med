<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div
			class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4"
		>
			<div>
				<h1 class="text-2xl md:text-3xl font-bold text-gray-900">Issued Blood</h1>
				<p class="text-gray-600">Manage issued blood units and track transfusions.</p>
			</div>
			<button
				class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
			>
				<span class="text-lg">+</span>
				Issue Blood
			</button>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
			<!-- Total Units Issued -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-sm font-medium text-gray-600 mb-2">Total Units Issued</h3>
				<div class="text-3xl font-bold text-gray-900 mb-2">19</div>
				<p class="text-sm text-green-600">+14 from last month</p>
			</div>

			<!-- Issued This Month -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-sm font-medium text-gray-600 mb-2">Issued This Month</h3>
				<div class="text-3xl font-bold text-gray-900 mb-2">32</div>
				<p class="text-sm text-green-600">+3 compared to last month</p>
			</div>

			<!-- Emergency Issues -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-sm font-medium text-gray-600 mb-2">Emergency Issues</h3>
				<div class="text-3xl font-bold text-gray-900 mb-2">2</div>
				<p class="text-sm text-gray-600">Critical situations handled</p>
			</div>

			<!-- Cross-Matched Units -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-sm font-medium text-gray-600 mb-2">Cross-Matched Units</h3>
				<div class="text-3xl font-bold text-gray-900 mb-2">13</div>
				<p class="text-sm text-gray-600">Compatibility verified</p>
			</div>
		</div>

		<!-- Charts Section -->
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
			<!-- Issues by Blood Type -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-6">Issues by Blood Type</h3>

				<div class="space-y-4">
					<div
						v-for="bloodType in bloodTypeIssues"
						:key="bloodType.type"
						class="flex items-center justify-between"
					>
						<div class="flex items-center gap-3 min-w-0 flex-1">
							<span class="text-sm font-medium text-gray-900 w-8">{{
								bloodType.type
							}}</span>
							<div class="flex-1 bg-gray-200 rounded-full h-2">
								<div
									class="h-2 rounded-full transition-all duration-300"
									:class="bloodType.color"
									:style="{
										width: `${(bloodType.units / maxBloodTypeUnits) * 100}%`,
									}"
								></div>
							</div>
						</div>
						<span class="text-sm text-gray-600 ml-4">{{ bloodType.units }} units</span>
					</div>
				</div>
			</div>

			<!-- Issues by Department -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-6">Issues by Department</h3>

				<div class="space-y-4">
					<div
						v-for="department in departmentIssues"
						:key="department.name"
						class="flex items-center justify-between"
					>
						<div class="flex items-center gap-3 min-w-0 flex-1">
							<span class="text-sm font-medium text-gray-900 w-20 truncate">{{
								department.name
							}}</span>
							<div class="flex-1 bg-gray-200 rounded-full h-2">
								<div
									class="h-2 rounded-full transition-all duration-300"
									:class="department.color"
									:style="{
										width: `${(department.units / maxDepartmentUnits) * 100}%`,
									}"
								></div>
							</div>
						</div>
						<span class="text-sm text-gray-600 ml-4"
							>{{ department.units }} units</span
						>
					</div>
				</div>
			</div>
		</div>

		<!-- Issues Table -->
		<div class="bg-white rounded-lg shadow-sm border">
			<!-- Filter Tabs -->
			<div class="border-b">
				<div class="flex gap-6 px-6 pt-4">
					<button
						v-for="tab in filterTabs"
						:key="tab.value"
						@click="activeTab = tab.value"
						:class="[
							'pb-4 text-sm font-medium border-b-2 transition-colors',
							activeTab === tab.value
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700',
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
								Issue ID
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Recipient
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Blood Type
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Issue Date
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Requesting Doctor
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Purpose
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
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
							v-for="issue in filteredIssues"
							:key="issue.id"
							class="hover:bg-gray-50"
						>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								{{ issue.id }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div class="flex-shrink-0 h-10 w-10">
										<div
											class="h-10 w-10 rounded-full flex items-center justify-center text-white text-sm font-medium"
											:class="issue.recipientAvatar"
										>
											{{ issue.recipientInitial }}
										</div>
									</div>
									<div class="ml-4">
										<div class="text-sm font-medium text-gray-900">
											{{ issue.recipientName }}
										</div>
										<div class="text-sm text-gray-500">
											{{ issue.recipientId }}
										</div>
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium text-white"
									:class="getBloodTypeColor(issue.bloodType)"
								>
									{{ issue.bloodType }} {{ issue.units }} unit(s)
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ issue.issueDate }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ issue.requestingDoctor }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ issue.purpose }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
									:class="getStatusColor(issue.status)"
								>
									{{ issue.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
								<button class="hover:text-gray-600">
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
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const activeTab = ref('all')

// Blood type issues data
const bloodTypeIssues = ref([
	{ type: 'A+', units: 2, color: 'bg-red-500' },
	{ type: 'A-', units: 1, color: 'bg-red-600' },
	{ type: 'AB+', units: 2, color: 'bg-purple-500' },
	{ type: 'AB-', units: 1, color: 'bg-purple-600' },
	{ type: 'B+', units: 3, color: 'bg-blue-500' },
	{ type: 'B-', units: 1, color: 'bg-blue-600' },
	{ type: 'O+', units: 8, color: 'bg-green-500' },
	{ type: 'O-', units: 1, color: 'bg-green-600' },
])

// Department issues data
const departmentIssues = ref([
	{ name: 'External', units: 6, color: 'bg-blue-500' },
	{ name: 'Emergency', units: 5, color: 'bg-green-500' },
	{ name: 'Surgery', units: 2, color: 'bg-yellow-500' },
	{ name: 'Cardiology', units: 2, color: 'bg-red-500' },
	{ name: 'Internal Medicine', units: 1, color: 'bg-purple-500' },
	{ name: 'Obstetrics', units: 1, color: 'bg-pink-500' },
	{ name: 'Oncology', units: 1, color: 'bg-indigo-500' },
	{ name: 'Nephrology', units: 1, color: 'bg-teal-500' },
])

// Filter tabs
const filterTabs = ref([
	{ label: 'All Issues', value: 'all' },
	{ label: 'Patient', value: 'patient' },
	{ label: 'External', value: 'external' },
	{ label: 'Emergency', value: 'emergency' },
])

// Issues data
const issues = ref([
	{
		id: 'ISS-2023-001',
		recipientName: 'John Smith',
		recipientId: 'PT-10045',
		recipientInitial: 'J',
		recipientAvatar: 'bg-blue-500',
		bloodType: 'O+',
		units: 2,
		issueDate: '2023-04-15 09:30 AM',
		requestingDoctor: 'Dr. Sarah Johnson',
		purpose: 'Surgery - Appendectomy',
		status: 'Delivered',
		category: 'patient',
	},
	{
		id: 'ISS-2023-002',
		recipientName: 'Emily Davis',
		recipientId: 'PT-10089',
		recipientInitial: 'E',
		recipientAvatar: 'bg-purple-500',
		bloodType: 'A+',
		units: 1,
		issueDate: '2023-04-16 02:15 PM',
		requestingDoctor: 'Dr. Michael Chen',
		purpose: 'Anemia Treatment',
		status: 'Delivered',
		category: 'patient',
	},
	{
		id: 'ISS-2023-003',
		recipientName: 'Robert Wilson',
		recipientId: 'PT-10124',
		recipientInitial: 'R',
		recipientAvatar: 'bg-gray-600',
		bloodType: 'B+',
		units: 3,
		issueDate: '2023-04-17 11:45 AM',
		requestingDoctor: 'Dr. Lisa Patel',
		purpose: 'Emergency - Trauma',
		status: 'Delivered',
		category: 'emergency',
	},
	{
		id: 'ISS-2023-004',
		recipientName: 'City Hospital',
		recipientId: 'EXT-0023',
		recipientInitial: 'C',
		recipientAvatar: 'bg-gray-700',
		bloodType: 'AB+',
		units: 2,
		issueDate: '2023-04-18 10:00 AM',
		requestingDoctor: 'Dr. James Wilson',
		purpose: 'External Request',
		status: 'In Transit',
		category: 'external',
	},
	{
		id: 'ISS-2023-005',
		recipientName: 'Maria Garcia',
		recipientId: 'PT-10156',
		recipientInitial: 'M',
		recipientAvatar: 'bg-green-500',
		bloodType: 'O+',
		units: 1,
		issueDate: '2023-04-19 03:30 PM',
		requestingDoctor: 'Dr. David Kim',
		purpose: 'Childbirth - Hemorrhage',
		status: 'Delivered',
		category: 'emergency',
	},
	{
		id: 'ISS-2023-006',
		recipientName: 'James Brown',
		recipientId: 'PT-10178',
		recipientInitial: 'J',
		recipientAvatar: 'bg-blue-500',
		bloodType: 'A+',
		units: 2,
		issueDate: '2023-04-20 08:45 AM',
		requestingDoctor: 'Dr. Emily White',
		purpose: 'Surgery - Heart Bypass',
		status: 'Delivered',
		category: 'patient',
	},
	{
		id: 'ISS-2023-007',
		recipientName: 'Linda Martinez',
		recipientId: 'PT-10203',
		recipientInitial: 'L',
		recipientAvatar: 'bg-green-500',
		bloodType: 'B+',
		units: 1,
		issueDate: '2023-04-21 01:30 PM',
		requestingDoctor: 'Dr. Robert Lee',
		purpose: 'Chemotherapy Support',
		status: 'Delivered',
		category: 'patient',
	},
	{
		id: 'ISS-2023-008',
		recipientName: 'County Medical Center',
		recipientId: 'EXT-0045',
		recipientInitial: 'C',
		recipientAvatar: 'bg-gray-700',
		bloodType: 'O+',
		units: 4,
		issueDate: '2023-04-22 09:15 AM',
		requestingDoctor: 'Dr. Thomas Brown',
		purpose: 'External Request',
		status: 'In Transit',
		category: 'external',
	},
	{
		id: 'ISS-2023-009',
		recipientName: 'William Taylor',
		recipientId: 'PT-10234',
		recipientInitial: 'W',
		recipientAvatar: 'bg-gray-600',
		bloodType: 'AB+',
		units: 1,
		issueDate: '2023-04-23 11:00 AM',
		requestingDoctor: 'Dr. Jennifer Garcia',
		purpose: 'Kidney Transplant',
		status: 'Delivered',
		category: 'patient',
	},
	{
		id: 'ISS-2023-010',
		recipientName: 'Sarah Johnson',
		recipientId: 'PT-10267',
		recipientInitial: 'S',
		recipientAvatar: 'bg-purple-500',
		bloodType: 'O+',
		units: 2,
		issueDate: '2023-04-24 02:45 PM',
		requestingDoctor: 'Dr. Mark Wilson',
		purpose: 'Emergency - Accident',
		status: 'Delivered',
		category: 'emergency',
	},
])

// Computed properties for chart scaling
const maxBloodTypeUnits = computed(() => {
	return Math.max(...bloodTypeIssues.value.map((item) => item.units))
})

const maxDepartmentUnits = computed(() => {
	return Math.max(...departmentIssues.value.map((item) => item.units))
})

// Filtered issues based on active tab
const filteredIssues = computed(() => {
	if (activeTab.value === 'all') {
		return issues.value
	}
	return issues.value.filter((issue) => issue.category === activeTab.value)
})

// Helper functions
const getBloodTypeColor = (bloodType) => {
	const colors = {
		'O+': 'bg-green-500',
		'O-': 'bg-green-600',
		'A+': 'bg-red-500',
		'A-': 'bg-red-600',
		'B+': 'bg-blue-500',
		'B-': 'bg-blue-600',
		'AB+': 'bg-purple-500',
		'AB-': 'bg-purple-600',
	}
	return colors[bloodType] || 'bg-gray-500'
}

const getStatusColor = (status) => {
	const colors = {
		Delivered: 'bg-green-100 text-green-800',
		'In Transit': 'bg-orange-100 text-orange-800',
		Pending: 'bg-yellow-100 text-yellow-800',
		Cancelled: 'bg-red-100 text-red-800',
	}
	return colors[status] || 'bg-gray-100 text-gray-800'
}
</script>

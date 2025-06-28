<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div
			class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4"
		>
			<div>
				<h1 class="text-2xl md:text-3xl font-bold text-gray-900">Blood Donors</h1>
				<p class="text-gray-600">Manage and track blood donors in your blood bank</p>
			</div>
			<button
				class="bg-black text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
			>
				<span class="text-lg">+</span>
				Register New Donor
			</button>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
			<!-- Total Donors -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<div class="flex items-center justify-between mb-2">
					<h3 class="text-sm font-medium text-gray-600">Total Donors</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"
							></path>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900">247</div>
				<p class="text-sm text-green-600">+12 from last month</p>
			</div>

			<!-- Donations This Month -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<div class="flex items-center justify-between mb-2">
					<h3 class="text-sm font-medium text-gray-600">Donations This Month</h3>
					<div class="p-2 bg-gray-100 rounded-lg">
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
								d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
							></path>
						</svg>
					</div>
				</div>
				<div class="text-3xl font-bold text-gray-900">38</div>
				<p class="text-sm text-green-600">+5 compared to last month</p>
			</div>

			<!-- Eligible Donors -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<div class="flex items-center justify-between mb-2">
					<h3 class="text-sm font-medium text-gray-600">Eligible Donors</h3>
					<span class="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full"
						>Active</span
					>
				</div>
				<div class="text-3xl font-bold text-gray-900">183</div>
				<p class="text-sm text-gray-600">Ready for donation</p>
			</div>

			<!-- Frequent Donors -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<div class="flex items-center justify-between mb-2">
					<h3 class="text-sm font-medium text-gray-600">Frequent Donors</h3>
					<span class="px-2 py-1 bg-purple-100 text-purple-800 text-xs rounded-full"
						>VIP</span
					>
				</div>
				<div class="text-3xl font-bold text-gray-900">42</div>
				<p class="text-sm text-gray-600">5+ donations</p>
			</div>
		</div>

		<!-- Charts Section -->
		<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
			<!-- Donors by Blood Type -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Donors by Blood Type</h3>
				<p class="text-sm text-gray-600 mb-6">
					Distribution of registered donors by blood type
				</p>

				<div class="grid grid-cols-4 gap-4 mb-6">
					<div v-for="bloodType in bloodTypes" :key="bloodType.type" class="text-center">
						<div
							class="h-24 rounded-lg mb-2"
							:class="bloodType.color"
							:style="{ height: `${bloodType.percentage * 2}px` }"
						></div>
						<div class="text-sm font-medium text-gray-900">{{ bloodType.type }}</div>
						<div class="text-xs text-gray-600">{{ bloodType.percentage }}%</div>
					</div>
				</div>
			</div>

			<!-- Donation Frequency -->
			<div class="bg-white p-6 rounded-lg shadow-sm border">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Donation Frequency</h3>
				<p class="text-sm text-gray-600 mb-6">Number of donors by donation frequency</p>

				<div class="space-y-4">
					<div
						v-for="frequency in donationFrequency"
						:key="frequency.label"
						class="flex items-center justify-between"
					>
						<div class="flex items-center gap-3">
							<div
								class="w-4 h-4 rounded-sm bg-gray-500"
								:style="{ opacity: frequency.opacity }"
							></div>
							<span class="text-sm font-medium text-gray-900">{{
								frequency.label
							}}</span>
						</div>
						<span class="text-lg font-bold text-gray-900">{{ frequency.count }}</span>
					</div>
				</div>
			</div>
		</div>

		<!-- Donors Table -->
		<div class="bg-white rounded-lg shadow-sm border">
			<!-- Table Header -->
			<div class="p-6 border-b">
				<div
					class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between"
				>
					<div class="flex flex-wrap gap-2">
						<div class="relative">
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search donors..."
								class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
							/>
							<svg
								class="absolute left-3 top-2.5 w-5 h-5 text-gray-400"
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

						<select
							v-model="selectedBloodType"
							class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
						>
							<option value="">All Blood Types</option>
							<option v-for="type in bloodTypes" :key="type.type" :value="type.type">
								{{ type.type }}
							</option>
						</select>

						<select
							v-model="selectedStatus"
							class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
						>
							<option value="">All Statuses</option>
							<option value="Eligible">Eligible</option>
							<option value="Ineligible">Ineligible</option>
							<option value="New">New</option>
						</select>

						<button class="p-2 border border-gray-300 rounded-lg hover:bg-gray-50">
							<svg
								class="w-5 h-5 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
								></path>
							</svg>
						</button>
					</div>

					<div class="flex gap-2">
						<button
							class="px-4 py-2 text-gray-600 hover:text-gray-900 flex items-center gap-2"
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
									d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
								></path>
							</svg>
							Refresh
						</button>
						<button
							class="px-4 py-2 text-gray-600 hover:text-gray-900 flex items-center gap-2"
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
									d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
								></path>
							</svg>
							Export
						</button>
					</div>
				</div>

				<!-- Filter Tabs -->
				<div class="flex gap-6 mt-4">
					<button
						v-for="tab in tabs"
						:key="tab.value"
						@click="activeTab = tab.value"
						:class="[
							'pb-2 text-sm font-medium border-b-2 transition-colors',
							activeTab === tab.value
								? 'border-blue-500 text-blue-600'
								: 'border-transparent text-gray-500 hover:text-gray-700',
						]"
					>
						{{ tab.label }}
					</button>
				</div>
			</div>

			<!-- Table Content -->
			<div class="overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Donor
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Blood Type
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Contact
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Last Donation
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Total Donations
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Next Eligible
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
							v-for="donor in filteredDonors"
							:key="donor.id"
							class="hover:bg-gray-50"
						>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div class="flex-shrink-0 h-10 w-10">
										<div
											class="h-10 w-10 rounded-full bg-gray-300 flex items-center justify-center"
										>
											<span class="text-sm font-medium text-gray-700">{{
												donor.name
													.split(' ')
													.map((n) => n[0])
													.join('')
											}}</span>
										</div>
									</div>
									<div class="ml-4">
										<div class="text-sm font-medium text-gray-900">
											{{ donor.name }}
										</div>
										<div class="text-sm text-gray-500">{{ donor.id }}</div>
									</div>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
									:class="getBloodTypeColor(donor.bloodType)"
								>
									{{ donor.bloodType }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								<div>{{ donor.phone }}</div>
								<div class="text-gray-500">{{ donor.email }}</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ donor.lastDonation }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
									:class="getStatusColor(donor.status)"
								>
									{{ donor.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center gap-2">
									<span class="text-sm font-medium text-gray-900">{{
										donor.totalDonations
									}}</span>
									<span
										v-if="donor.badge"
										class="px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full"
										>{{ donor.badge }}</span
									>
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								{{ donor.nextEligible }}
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
const searchQuery = ref('')
const selectedBloodType = ref('')
const selectedStatus = ref('')
const activeTab = ref('all')

// Static data
const bloodTypes = ref([
	{ type: 'O+', percentage: 38, color: 'bg-red-500' },
	{ type: 'A+', percentage: 18, color: 'bg-blue-500' },
	{ type: 'B+', percentage: 12, color: 'bg-green-500' },
	{ type: 'AB+', percentage: 6, color: 'bg-purple-500' },
	{ type: 'O-', percentage: 9, color: 'bg-red-600' },
	{ type: 'A-', percentage: 7, color: 'bg-blue-600' },
	{ type: 'B-', percentage: 6, color: 'bg-green-600' },
	{ type: 'AB-', percentage: 4, color: 'bg-purple-600' },
])

const donationFrequency = ref([
	{ label: 'First Time', count: 98, opacity: 1 },
	{ label: '2-4 Times', count: 107, opacity: 0.8 },
	{ label: '5-9 Times', count: 24, opacity: 0.6 },
	{ label: '10-24 Times', count: 12, opacity: 0.4 },
	{ label: '25+ Times', count: 6, opacity: 0.2 },
])

const tabs = ref([
	{ label: 'All Donors', value: 'all' },
	{ label: 'Eligible', value: 'eligible' },
	{ label: 'Ineligible', value: 'ineligible' },
	{ label: 'New', value: 'new' },
])

const donors = ref([
	{
		id: 'D-1001',
		name: 'John Smith',
		bloodType: 'O+',
		phone: '+1 (555) 123-4567',
		email: 'john.smith@example.com',
		lastDonation: '15/03/2023',
		status: 'Eligible',
		totalDonations: 8,
		badge: 'Silver Donor',
		nextEligible: '15/07/2023',
	},
	{
		id: 'D-1002',
		name: 'Sarah Johnson',
		bloodType: 'A+',
		phone: '+1 (555) 987-6543',
		email: 'sarah.johnson@example.com',
		lastDonation: '22/02/2023',
		status: 'Eligible',
		totalDonations: 12,
		badge: 'Gold Donor',
		nextEligible: '22/06/2023',
	},
	{
		id: 'D-1003',
		name: 'Michael Brown',
		bloodType: 'B+',
		phone: '+1 (555) 456-7890',
		email: 'michael.brown@example.com',
		lastDonation: '10/01/2023',
		status: 'Ineligible',
		totalDonations: 3,
		badge: null,
		nextEligible: '10/05/2023',
	},
	{
		id: 'D-1004',
		name: 'Emma Davis',
		bloodType: 'AB+',
		phone: '+1 (555) 321-0987',
		email: 'emma.davis@example.com',
		lastDonation: 'Never',
		status: 'New',
		totalDonations: 0,
		badge: null,
		nextEligible: 'Eligible Now',
	},
])

// Computed properties
const filteredDonors = computed(() => {
	let filtered = donors.value

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(donor) =>
				donor.name.toLowerCase().includes(query) ||
				donor.id.toLowerCase().includes(query) ||
				donor.email.toLowerCase().includes(query),
		)
	}

	// Filter by blood type
	if (selectedBloodType.value) {
		filtered = filtered.filter((donor) => donor.bloodType === selectedBloodType.value)
	}

	// Filter by status
	if (selectedStatus.value) {
		filtered = filtered.filter((donor) => donor.status === selectedStatus.value)
	}

	// Filter by active tab
	if (activeTab.value !== 'all') {
		filtered = filtered.filter((donor) => donor.status.toLowerCase() === activeTab.value)
	}

	return filtered
})

// Helper functions
const getBloodTypeColor = (bloodType) => {
	const colors = {
		'O+': 'bg-red-100 text-red-800',
		'A+': 'bg-blue-100 text-blue-800',
		'B+': 'bg-green-100 text-green-800',
		'AB+': 'bg-purple-100 text-purple-800',
		'O-': 'bg-red-200 text-red-900',
		'A-': 'bg-blue-200 text-blue-900',
		'B-': 'bg-green-200 text-green-900',
		'AB-': 'bg-purple-200 text-purple-900',
	}
	return colors[bloodType] || 'bg-gray-100 text-gray-800'
}

const getStatusColor = (status) => {
	const colors = {
		Eligible: 'bg-green-100 text-green-800',
		Ineligible: 'bg-red-100 text-red-800',
		New: 'bg-blue-100 text-blue-800',
	}
	return colors[status] || 'bg-gray-100 text-gray-800'
}
</script>

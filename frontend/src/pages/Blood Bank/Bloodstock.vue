<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="mb-8">
			<h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">Blood Stock</h1>
			<p class="text-gray-600">Manage and monitor blood inventory in the blood bank</p>
		</div>

		<!-- Stats Cards -->
		<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-8">
			<!-- Total Blood Units -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center">
						<svg class="w-5 h-5 text-red-600" fill="currentColor" viewBox="0 0 20 20">
							<path
								fill-rule="evenodd"
								d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
								clip-rule="evenodd"
							/>
						</svg>
					</div>
					<button class="text-red-500 hover:text-red-600">
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							/>
						</svg>
					</button>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Total Blood Units</p>
					<p class="text-2xl font-bold text-gray-900">{{ totalBloodUnits }}</p>
				</div>
				<p class="text-xs text-gray-500">Units available across all blood types</p>
			</div>

			<!-- Blood Type Distribution -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
						<svg
							class="w-5 h-5 text-blue-600"
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
					<button class="text-red-500 hover:text-red-600">
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							/>
						</svg>
					</button>
				</div>
				<div class="mb-4">
					<p class="text-sm font-medium text-gray-600 mb-3">Blood Type Distribution</p>
					<div class="grid grid-cols-4 gap-2">
						<div
							v-for="(blood, index) in bloodTypeDistribution"
							:key="index"
							class="text-center"
						>
							<span
								:class="getBloodTypeBadgeClass(blood.type)"
								class="inline-block px-2 py-1 rounded text-xs font-medium mb-1"
							>
								{{ blood.type }}
							</span>
							<p class="text-xs text-gray-600">{{ blood.count }}</p>
						</div>
					</div>
				</div>
			</div>

			<!-- Expiring Soon -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div
						class="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center"
					>
						<div
							class="w-6 h-6 bg-orange-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">!</span>
						</div>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Expiring Soon</p>
					<p class="text-2xl font-bold text-gray-900">10</p>
				</div>
				<p class="text-xs text-gray-500">Units expiring within the next 7 days</p>
			</div>

			<!-- Critical Levels -->
			<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
				<div class="flex items-center justify-between mb-4">
					<div class="w-10 h-10 bg-red-100 rounded-lg flex items-center justify-center">
						<div
							class="w-6 h-6 bg-red-500 rounded-full flex items-center justify-center"
						>
							<span class="text-white text-xs font-bold">!</span>
						</div>
					</div>
				</div>
				<div class="mb-2">
					<p class="text-sm font-medium text-gray-600 mb-1">Critical Levels</p>
					<p class="text-2xl font-bold text-gray-900">2</p>
				</div>
				<p class="text-xs text-gray-500">Blood types with critically low inventory</p>
			</div>
		</div>

		<!-- Blood Type Availability Chart -->
		<div class="bg-white rounded-xl p-6 shadow-sm border border-gray-100 mb-8">
			<div class="mb-6">
				<h2 class="text-lg font-semibold text-gray-900 mb-2">Blood Type Availability</h2>
				<p class="text-sm text-gray-600">Current inventory levels for each blood type</p>
			</div>

			<div class="space-y-6">
				<div
					v-for="bloodType in bloodAvailability"
					:key="bloodType.type"
					class="flex items-center"
				>
					<!-- Blood Type Label -->
					<div class="w-12 text-right mr-4">
						<span class="text-sm font-medium text-gray-900">{{ bloodType.type }}</span>
					</div>

					<!-- Progress Bar Container -->
					<div class="flex-1 mr-4">
						<div class="bg-gray-200 rounded-full h-6 relative overflow-hidden">
							<div
								:class="getProgressBarClass(bloodType.level)"
								class="h-full rounded-full transition-all duration-500 ease-out"
								:style="{ width: getProgressWidth(bloodType.units) + '%' }"
							></div>
						</div>
					</div>

					<!-- Units Count -->
					<div class="w-16 text-right">
						<span class="text-sm font-semibold text-gray-900">{{
							bloodType.units
						}}</span>
						<span class="text-xs text-gray-500 ml-1">units</span>
					</div>
				</div>
			</div>

			<!-- Legend -->
			<div class="mt-8 pt-6 border-t border-gray-200">
				<div class="flex flex-wrap gap-4 text-xs">
					<div class="flex items-center">
						<div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
						<span class="text-gray-600">Good Stock (8+ units)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-orange-500 rounded-full mr-2"></div>
						<span class="text-gray-600">Low Stock (3-7 units)</span>
					</div>
					<div class="flex items-center">
						<div class="w-3 h-3 bg-red-500 rounded-full mr-2"></div>
						<span class="text-gray-600">Critical Stock (1-2 units)</span>
					</div>
				</div>
			</div>
		</div>

		<!-- Blood Units Management Section -->
		<div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
			<!-- Search and Filters -->
			<div class="p-6 border-b border-gray-200">
				<div class="flex flex-col lg:flex-row gap-4">
					<!-- Search -->
					<div class="flex-1">
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
								/>
							</svg>
							<input
								v-model="searchQuery"
								type="text"
								placeholder="Search blood units..."
								class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 outline-none"
							/>
						</div>
					</div>

					<!-- Filters -->
					<div class="flex flex-col sm:flex-row gap-4">
						<select
							v-model="selectedBloodType"
							class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 outline-none min-w-[120px]"
						>
							<option value="">All Types</option>
							<option v-for="type in bloodTypes" :key="type" :value="type">
								{{ type }}
							</option>
						</select>

						<select
							v-model="selectedStatus"
							class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 outline-none min-w-[120px]"
						>
							<option value="">All Status</option>
							<option value="Available">Available</option>
							<option value="Reserved">Reserved</option>
							<option value="Expiring Soon">Expiring Soon</option>
						</select>

						<!-- Action Buttons -->
						<div class="flex gap-2">
							<button
								class="px-3 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center gap-2"
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
										d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.707A1 1 0 013 7V4z"
									/>
								</svg>
							</button>

							<button
								class="px-3 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center gap-2"
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
										d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
									/>
								</svg>
							</button>

							<button
								class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center gap-2"
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
									/>
								</svg>
								Refresh
							</button>

							<button
								class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors flex items-center gap-2"
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
									/>
								</svg>
								Export
							</button>

							<button
								class="bg-gray-900 text-white px-4 py-2 rounded-lg hover:bg-gray-800 transition-colors flex items-center gap-2"
							>
								<span class="text-lg">+</span>
								Add Blood Units
							</button>
						</div>
					</div>
				</div>

				<!-- Filter Tabs -->
				<div class="flex gap-6 mt-6 border-b border-gray-200">
					<button
						v-for="tab in filterTabs"
						:key="tab"
						@click="activeTab = tab"
						:class="[
							'pb-2 px-1 text-sm font-medium border-b-2 transition-colors',
							activeTab === tab
								? 'text-red-600 border-red-600'
								: 'text-gray-500 border-transparent hover:text-gray-700',
						]"
					>
						{{ tab }}
					</button>
				</div>
			</div>

			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50 border-b border-gray-200">
						<tr>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								ID
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Blood Type
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Units
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Collection Date
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Expiry Date
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Status
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Location
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Donor
							</th>
							<th
								class="text-left py-4 px-6 text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Actions
							</th>
						</tr>
					</thead>
					<tbody class="divide-y divide-gray-200">
						<tr
							v-for="unit in filteredBloodUnits"
							:key="unit.id"
							class="hover:bg-gray-50"
						>
							<td class="py-4 px-6">
								<span class="text-sm font-medium text-blue-600">{{
									unit.id
								}}</span>
							</td>
							<td class="py-4 px-6">
								<span class="text-sm font-semibold text-gray-900">{{
									unit.bloodType
								}}</span>
							</td>
							<td class="py-4 px-6 text-sm text-gray-600">{{ unit.units }}</td>
							<td class="py-4 px-6 text-sm text-gray-600">
								{{ unit.collectionDate }}
							</td>
							<td class="py-4 px-6 text-sm text-gray-600">{{ unit.expiryDate }}</td>
							<td class="py-4 px-6">
								<span
									:class="getStatusBadgeClass(unit.status)"
									class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
								>
									{{ unit.status }}
								</span>
							</td>
							<td class="py-4 px-6 text-sm text-gray-600">{{ unit.location }}</td>
							<td class="py-4 px-6">
								<span
									class="text-sm font-medium text-blue-600 hover:text-blue-800 cursor-pointer"
									>{{ unit.donor }}</span
								>
							</td>
							<td class="py-4 px-6">
								<button class="text-gray-400 hover:text-gray-600">
									<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
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

			<!-- Mobile Cards -->
			<div class="lg:hidden">
				<div
					v-for="unit in filteredBloodUnits"
					:key="unit.id"
					class="p-4 border-b border-gray-200 last:border-b-0"
				>
					<div class="flex justify-between items-start mb-3">
						<div class="flex-1">
							<div class="flex items-center gap-2 mb-1">
								<span class="text-sm font-medium text-blue-600">{{
									unit.id
								}}</span>
								<span class="text-sm font-semibold text-gray-900">{{
									unit.bloodType
								}}</span>
							</div>
							<p class="text-xs text-gray-500">{{ unit.donor }}</p>
						</div>
						<span
							:class="getStatusBadgeClass(unit.status)"
							class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ml-2"
						>
							{{ unit.status }}
						</span>
					</div>

					<div class="grid grid-cols-2 gap-4 text-xs">
						<div>
							<p class="text-gray-500">Units</p>
							<p class="text-gray-900 font-medium">{{ unit.units }}</p>
						</div>
						<div>
							<p class="text-gray-500">Location</p>
							<p class="text-gray-900 font-medium">{{ unit.location }}</p>
						</div>
						<div>
							<p class="text-gray-500">Collection Date</p>
							<p class="text-gray-900 font-medium">{{ unit.collectionDate }}</p>
						</div>
						<div>
							<p class="text-gray-500">Expiry Date</p>
							<p class="text-gray-900 font-medium">{{ unit.expiryDate }}</p>
						</div>
					</div>
				</div>
			</div>

			<!-- Pagination -->
			<div class="px-6 py-4 border-t border-gray-200 flex items-center justify-between">
				<div class="text-sm text-gray-500">
					Showing {{ startIndex + 1 }}-{{ endIndex }} of
					{{ filteredBloodUnits.length }} units
				</div>
				<div class="flex gap-2">
					<button
						@click="previousPage"
						:disabled="currentPage === 1"
						:class="[
							'px-3 py-1 text-sm rounded border',
							currentPage === 1
								? 'text-gray-400 border-gray-200 cursor-not-allowed'
								: 'text-gray-700 border-gray-300 hover:bg-gray-50',
						]"
					>
						Previous
					</button>
					<button
						@click="nextPage"
						:disabled="currentPage === totalPages"
						:class="[
							'px-3 py-1 text-sm rounded border',
							currentPage === totalPages
								? 'text-gray-400 border-gray-200 cursor-not-allowed'
								: 'text-gray-700 border-gray-300 hover:bg-gray-50',
						]"
					>
						Next
					</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive filters and search
const searchQuery = ref('')
const selectedBloodType = ref('')
const selectedStatus = ref('')
const activeTab = ref('All Units')
const currentPage = ref(1)
const itemsPerPage = 8

// Filter tabs
const filterTabs = ['All Units', 'Available', 'Reserved', 'Expiring Soon']

// Blood types for filter dropdown
const bloodTypes = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

// Blood type distribution data
const bloodTypeDistribution = ref([
	{ type: 'A+', count: 12 },
	{ type: 'A-', count: 4 },
	{ type: 'B+', count: 8 },
	{ type: 'B-', count: 2 },
	{ type: 'AB+', count: 3 },
	{ type: 'AB-', count: 1 },
	{ type: 'O+', count: 15 },
	{ type: 'O-', count: 5 },
])

// Blood availability data with levels
const bloodAvailability = ref([
	{ type: 'A+', units: 12, level: 'good' },
	{ type: 'A-', units: 4, level: 'low' },
	{ type: 'B+', units: 8, level: 'good' },
	{ type: 'B-', units: 2, level: 'critical' },
	{ type: 'AB+', units: 3, level: 'low' },
	{ type: 'AB-', units: 1, level: 'critical' },
	{ type: 'O+', units: 15, level: 'good' },
	{ type: 'O-', units: 5, level: 'low' },
])

// Blood units data
const bloodUnits = ref([
	{
		id: 'BS-001',
		bloodType: 'A+',
		units: 12,
		collectionDate: '2023-04-15',
		expiryDate: '2023-05-15',
		status: 'Available',
		location: 'Refrigerator 1',
		donor: 'John Smith',
	},
	{
		id: 'BS-002',
		bloodType: 'O-',
		units: 5,
		collectionDate: '2023-04-16',
		expiryDate: '2023-05-16',
		status: 'Reserved',
		location: 'Refrigerator 2',
		donor: 'Emily Johnson',
	},
	{
		id: 'BS-003',
		bloodType: 'B+',
		units: 8,
		collectionDate: '2023-04-10',
		expiryDate: '2023-05-10',
		status: 'Expiring Soon',
		location: 'Refrigerator 1',
		donor: 'Michael Brown',
	},
	{
		id: 'BS-004',
		bloodType: 'AB+',
		units: 3,
		collectionDate: '2023-04-12',
		expiryDate: '2023-05-12',
		status: 'Available',
		location: 'Refrigerator 3',
		donor: 'Sarah Davis',
	},
	{
		id: 'BS-005',
		bloodType: 'A-',
		units: 4,
		collectionDate: '2023-04-14',
		expiryDate: '2023-05-14',
		status: 'Available',
		location: 'Refrigerator 2',
		donor: 'Robert Wilson',
	},
	{
		id: 'BS-006',
		bloodType: 'O+',
		units: 15,
		collectionDate: '2023-04-13',
		expiryDate: '2023-05-13',
		status: 'Available',
		location: 'Refrigerator 1',
		donor: 'Jennifer Taylor',
	},
	{
		id: 'BS-007',
		bloodType: 'B-',
		units: 2,
		collectionDate: '2023-04-08',
		expiryDate: '2023-05-08',
		status: 'Expiring Soon',
		location: 'Refrigerator 3',
		donor: 'David Martinez',
	},
	{
		id: 'BS-008',
		bloodType: 'AB-',
		units: 1,
		collectionDate: '2023-04-11',
		expiryDate: '2023-05-11',
		status: 'Reserved',
		location: 'Refrigerator 2',
		donor: 'Lisa Anderson',
	},
])

// Computed properties
const totalBloodUnits = computed(() => {
	return bloodAvailability.value.reduce((total, blood) => total + blood.units, 0)
})

const maxUnits = computed(() => {
	return Math.max(...bloodAvailability.value.map((blood) => blood.units))
})

const filteredBloodUnits = computed(() => {
	return bloodUnits.value.filter((unit) => {
		const matchesSearch =
			unit.id.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			unit.bloodType.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			unit.donor.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			unit.location.toLowerCase().includes(searchQuery.value.toLowerCase())

		const matchesBloodType =
			!selectedBloodType.value || unit.bloodType === selectedBloodType.value
		const matchesStatus = !selectedStatus.value || unit.status === selectedStatus.value
		const matchesTab = activeTab.value === 'All Units' || unit.status === activeTab.value

		return matchesSearch && matchesBloodType && matchesStatus && matchesTab
	})
})

const totalPages = computed(() => {
	return Math.ceil(filteredBloodUnits.value.length / itemsPerPage)
})

const startIndex = computed(() => {
	return (currentPage.value - 1) * itemsPerPage
})

const endIndex = computed(() => {
	return Math.min(startIndex.value + itemsPerPage, filteredBloodUnits.value.length)
})

// Methods
const getBloodTypeBadgeClass = (type) => {
	// Color coding based on blood type rarity/criticality
	const criticalTypes = ['B-', 'AB-']
	const lowTypes = ['A-', 'AB+', 'O-']

	if (criticalTypes.includes(type)) {
		return 'bg-red-100 text-red-800'
	} else if (lowTypes.includes(type)) {
		return 'bg-orange-100 text-orange-800'
	} else {
		return 'bg-green-100 text-green-800'
	}
}

const getProgressBarClass = (level) => {
	switch (level) {
		case 'good':
			return 'bg-green-500'
		case 'low':
			return 'bg-orange-500'
		case 'critical':
			return 'bg-red-500'
		default:
			return 'bg-gray-400'
	}
}

const getProgressWidth = (units) => {
	// Calculate percentage based on max units (15), with minimum width for visibility
	const percentage = (units / maxUnits.value) * 100
	return Math.max(percentage, 8) // Minimum 8% width for visibility
}

const getStatusBadgeClass = (status) => {
	switch (status) {
		case 'Available':
			return 'bg-green-100 text-green-800'
		case 'Reserved':
			return 'bg-gray-100 text-gray-800'
		case 'Expiring Soon':
			return 'bg-orange-100 text-orange-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

const nextPage = () => {
	if (currentPage.value < totalPages.value) {
		currentPage.value++
	}
}

const previousPage = () => {
	if (currentPage.value > 1) {
		currentPage.value--
	}
}
</script>

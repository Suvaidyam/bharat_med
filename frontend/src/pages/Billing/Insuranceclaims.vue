<template>
	<div class="min-h-screen p-4 md:p-6">
		<!-- Header -->
		<div class="mb-6">
			<div class="flex items-center mb-4">
				<button class="mr-4 p-2 hover:bg-gray-100 rounded-lg">
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
							d="M15 19l-7-7 7-7"
						></path>
					</svg>
				</button>
				<div>
					<h1 class="text-2xl font-semibold text-gray-900">Insurance Claims</h1>
					<p class="text-sm text-gray-500">
						Manage and track insurance claims for patient services.
					</p>
				</div>
			</div>

			<!-- Search and Filters -->
			<div
				class="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between"
			>
				<div class="flex flex-col sm:flex-row gap-4 flex-1">
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
							placeholder="Search claims..."
							class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full sm:w-64"
						/>
					</div>
					<button
						class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 flex items-center"
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
						class="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 flex items-center"
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
				<div class="text-sm text-gray-500">Jun 28, 2025 - Jun 28, 2025</div>
			</div>
		</div>

		<!-- Tabs -->
		<div class="mb-6">
			<div class="flex space-x-1 bg-gray-100 rounded-lg p-1 w-fit">
				<button
					v-for="tab in tabs"
					:key="tab.id"
					@click="activeTab = tab.id"
					:class="[
						'px-4 py-2 rounded-md text-sm font-medium transition-colors',
						activeTab === tab.id
							? 'bg-white text-gray-900 shadow-sm'
							: 'text-gray-600 hover:text-gray-900',
					]"
				>
					{{ tab.label }}
				</button>
			</div>
		</div>

		<!-- Main Content -->
		<div class="bg-white rounded-lg shadow">
			<!-- Table Header -->
			<div class="px-6 py-4 border-b border-gray-200">
				<div class="flex items-center justify-between">
					<h2 class="text-lg font-medium text-gray-900">All Insurance Claims</h2>
					<select
						v-model="sortOrder"
						class="text-sm border border-gray-300 rounded px-3 py-1"
					>
						<option value="newest">Newest First</option>
						<option value="oldest">Oldest First</option>
						<option value="amount-high">Amount: High to Low</option>
						<option value="amount-low">Amount: Low to High</option>
					</select>
				</div>
				<p class="text-sm text-gray-500 mt-1">View and manage all insurance claims.</p>
			</div>

			<!-- Desktop Table -->
			<div class="hidden lg:block overflow-x-auto">
				<table class="w-full">
					<thead class="bg-gray-50">
						<tr>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Claim ID
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Patient
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Provider
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Submitted
							</th>
							<th
								class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Amount
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
								Actions
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr
							v-for="claim in filteredClaims"
							:key="claim.id"
							class="hover:bg-gray-50"
						>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								{{ claim.id }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<div class="flex items-center">
									<div class="flex-shrink-0 h-8 w-8">
										<div
											class="h-8 w-8 rounded-full bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center"
										>
											<span class="text-white text-sm font-medium">{{
												getInitials(claim.patient.name)
											}}</span>
										</div>
									</div>
									<div class="ml-3">
										<div class="text-sm font-medium text-gray-900">
											{{ claim.patient.name }}
										</div>
										<div class="text-sm text-gray-500">
											{{ claim.patient.id }}
										</div>
									</div>
								</div>
							</td>
							<td class="px-6 py-4">
								<div class="text-sm text-gray-900">{{ claim.provider.name }}</div>
								<div class="text-sm text-gray-500">
									Policy: {{ claim.provider.policy }}
								</div>
							</td>
							<td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
								<span v-if="claim.submitted !== 'Not submitted'">{{
									claim.submitted
								}}</span>
								<span v-else class="text-gray-500 italic">{{
									claim.submitted
								}}</span>
							</td>
							<td
								class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
							>
								${{ claim.amount.toFixed(2) }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getStatusClass(claim.status)"
									class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
								>
									{{ claim.status }}
								</span>
							</td>
							<td class="px-6 py-4 whitespace-nowrap">
								<span
									:class="getTypeClass(claim.type)"
									class="inline-flex px-2 py-1 text-xs font-medium rounded"
								>
									{{ claim.type }}
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

			<!-- Mobile Cards -->
			<div class="lg:hidden">
				<div
					v-for="claim in filteredClaims"
					:key="claim.id"
					class="border-b border-gray-200 p-4"
				>
					<div class="flex items-center justify-between mb-3">
						<div class="flex items-center">
							<div
								class="h-10 w-10 rounded-full bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center mr-3"
							>
								<span class="text-white text-sm font-medium">{{
									getInitials(claim.patient.name)
								}}</span>
							</div>
							<div>
								<div class="font-medium text-gray-900">
									{{ claim.patient.name }}
								</div>
								<div class="text-sm text-gray-500">{{ claim.patient.id }}</div>
							</div>
						</div>
						<span
							:class="getStatusClass(claim.status)"
							class="inline-flex px-2 py-1 text-xs font-medium rounded-full"
						>
							{{ claim.status }}
						</span>
					</div>
					<div class="grid grid-cols-2 gap-3 text-sm">
						<div>
							<span class="text-gray-500">Claim ID:</span>
							<div class="font-medium">{{ claim.id }}</div>
						</div>
						<div>
							<span class="text-gray-500">Provider:</span>
							<div class="font-medium">{{ claim.provider.name }}</div>
						</div>
						<div>
							<span class="text-gray-500">Submitted:</span>
							<div class="font-medium">
								<span v-if="claim.submitted !== 'Not submitted'">{{
									claim.submitted
								}}</span>
								<span v-else class="text-gray-500 italic">{{
									claim.submitted
								}}</span>
							</div>
						</div>
						<div>
							<span class="text-gray-500">Amount:</span>
							<div class="font-medium">${{ claim.amount.toFixed(2) }}</div>
						</div>
						<div>
							<span class="text-gray-500">Type:</span>
							<div>
								<span
									:class="getTypeClass(claim.type)"
									class="inline-flex px-2 py-1 text-xs font-medium rounded"
								>
									{{ claim.type }}
								</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Statistics Cards -->
		<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Total Claims</h3>
				<div class="text-3xl font-bold text-gray-900">${{ stats.total.toFixed(2) }}</div>
				<div class="text-sm text-gray-500">From {{ stats.totalCount }} claims</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div class="bg-gray-900 h-2 rounded-full" style="width: 100%"></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Approved Claims</h3>
				<div class="text-3xl font-bold text-green-600">
					${{ stats.approved.toFixed(2) }}
				</div>
				<div class="text-sm text-gray-500">From {{ stats.approvedCount }} claims</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div
						class="bg-green-500 h-2 rounded-full"
						:style="`width: ${(stats.approved / stats.total) * 100}%`"
					></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Pending Claims</h3>
				<div class="text-3xl font-bold text-orange-600">
					${{ stats.pending.toFixed(2) }}
				</div>
				<div class="text-sm text-gray-500">From {{ stats.pendingCount }} claims</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div
						class="bg-orange-500 h-2 rounded-full"
						:style="`width: ${(stats.pending / stats.total) * 100}%`"
					></div>
				</div>
			</div>

			<div class="bg-white rounded-lg shadow p-6">
				<h3 class="text-lg font-medium text-gray-900 mb-2">Claim Success Rate</h3>
				<div class="text-3xl font-bold text-gray-900">{{ successRate }}%</div>
				<div class="text-sm text-gray-500">Approved rate for submitted claims</div>
				<div class="w-full bg-gray-200 rounded-full h-2 mt-3">
					<div
						class="bg-gray-900 h-2 rounded-full"
						:style="`width: ${successRate}%`"
					></div>
				</div>
			</div>
		</div>
		<div class="p-6 mt-4 bg-white rounded-lg shadow">
			<!-- Header -->
			<div class="mb-4">
				<h2 class="text-xl font-semibold text-gray-800">Claim Details</h2>
				<p class="text-sm text-gray-500">
					View detailed information about a selected claim.
				</p>
			</div>

			<!-- Claim Summary -->
			<div class="mb-6">
				<p class="text-sm text-gray-700 font-medium">Claim CLM-001</p>
				<p class="text-sm text-gray-500">
					Blue Cross Blue Shield • Submitted on 2024-04-15
				</p>
			</div>

			<!-- Main Info Grid -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
				<!-- Patient Information -->
				<div>
					<h3 class="text-sm font-semibold text-gray-700 mb-2">Patient Information</h3>
					<div class="flex items-center gap-3 mb-2">
						<img
							src="https://via.placeholder.com/40"
							class="w-10 h-10 rounded-full"
							alt="Patient Avatar"
						/>
						<div>
							<p class="text-sm font-medium text-gray-800">John Smith</p>
							<p class="text-xs text-gray-500">ID: P12345</p>
						</div>
					</div>
					<ul class="text-sm text-gray-600 space-y-1">
						<li><strong>Policy Number:</strong> BCBS123456789</li>
						<li><strong>Group Number:</strong> GRP987654321</li>
						<li><strong>Relationship:</strong> Self</li>
					</ul>
				</div>

				<!-- Claim Information -->
				<div class="relative">
					<h3 class="text-sm font-semibold text-gray-700 mb-2">Claim Information</h3>
					<ul class="text-sm text-gray-600 space-y-1">
						<li><strong>Claim Type:</strong> Medical</li>
						<li><strong>Claim Amount:</strong> $200.00</li>
						<li><strong>Approved Amount:</strong> $180.00</li>
						<li><strong>Patient Responsibility:</strong> $20.00</li>
						<li><strong>Payment Date:</strong> 2024-04-22</li>
					</ul>
					<span
						class="absolute top-0 right-0 bg-green-100 text-green-700 text-xs font-semibold px-2 py-1 rounded-full"
						>Approved</span
					>
				</div>
			</div>

			<!-- Services & Procedures Table -->
			<div class="mt-8">
				<h3 class="text-sm font-semibold text-gray-700 mb-3">Services & Procedures</h3>
				<div class="overflow-auto">
					<table class="min-w-full text-sm text-left text-gray-600">
						<thead class="bg-gray-100 text-gray-700 uppercase">
							<tr>
								<th class="px-4 py-2">Service</th>
								<th class="px-4 py-2">Date</th>
								<th class="px-4 py-2">Billed</th>
								<th class="px-4 py-2">Allowed</th>
								<th class="px-4 py-2">Patient Resp.</th>
							</tr>
						</thead>
						<tbody>
							<tr class="border-b">
								<td class="px-4 py-2">General Consultation</td>
								<td class="px-4 py-2">2024-04-15</td>
								<td class="px-4 py-2">$150.00</td>
								<td class="px-4 py-2">$135.00</td>
								<td class="px-4 py-2">$15.00</td>
							</tr>
							<tr>
								<td class="px-4 py-2">Blood Test – Basic Panel</td>
								<td class="px-4 py-2">2024-04-15</td>
								<td class="px-4 py-2">$50.00</td>
								<td class="px-4 py-2">$45.00</td>
								<td class="px-4 py-2">$5.00</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>

			<!-- Notes -->
			<div class="mt-6 text-sm text-gray-600">
				<h3 class="font-semibold mb-1">Notes</h3>
				<p>Claim approved with standard copay deduction</p>
			</div>

			<!-- Action Buttons -->
			<div class="mt-6 flex flex-wrap gap-3">
				<button
					class="flex items-center px-4 py-2 text-sm bg-gray-100 hover:bg-gray-200 rounded"
				>
					<span class="material-icons text-base mr-1">download</span>
					Download EOB
				</button>
				<button
					class="flex items-center px-4 py-2 text-sm bg-gray-100 hover:bg-gray-200 rounded"
				>
					<span class="material-icons text-base mr-1">visibility</span>
					View Invoice
				</button>
				<button
					class="flex items-center px-4 py-2 text-sm bg-black text-white hover:bg-gray-800 rounded"
				>
					<span class="material-icons text-base mr-1">check_circle</span>
					Mark as Reconciled
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Reactive data
const searchQuery = ref('')
const activeTab = ref('all')
const sortOrder = ref('newest')

const tabs = [
	{ id: 'all', label: 'All Claims' },
	{ id: 'approved', label: 'Approved' },
	{ id: 'pending', label: 'Pending' },
	{ id: 'rejected', label: 'Rejected' },
	{ id: 'draft', label: 'Draft' },
]

const claims = ref([
	{
		id: 'CLM-001',
		patient: { name: 'John Smith', id: '678945' },
		provider: { name: 'Blue Cross Blue Shield', policy: 'BC851245789' },
		submitted: '2024-04-15',
		amount: 200.0,
		status: 'Approved',
		type: 'Medical',
	},
	{
		id: 'CLM-002',
		patient: { name: 'Emily Davis', id: '723456' },
		provider: { name: 'Aetna', policy: 'AET967854321' },
		submitted: '2024-04-16',
		amount: 280.0,
		status: 'Pending',
		type: 'Medical',
	},
	{
		id: 'CLM-003',
		patient: { name: 'Robert Wilson', id: '456789' },
		provider: { name: 'UnitedHealthcare', policy: 'UH520960234' },
		submitted: '2024-04-10',
		amount: 140.0,
		status: 'Approved',
		type: 'Medical',
	},
	{
		id: 'CLM-004',
		patient: { name: 'Jessica Brown', id: '389745' },
		provider: { name: 'Delta Dental', policy: 'DD456980123' },
		submitted: '2024-04-05',
		amount: 416.0,
		status: 'Approved',
		type: 'Dental',
	},
	{
		id: 'CLM-005',
		patient: { name: 'Michael Johnson', id: '506789' },
		provider: { name: 'Cigna', policy: 'CIG123789456' },
		submitted: '2024-04-18',
		amount: 360.0,
		status: 'Submitted',
		type: 'Medical',
	},
	{
		id: 'CLM-006',
		patient: { name: 'Sarah Thompson', id: '234567' },
		provider: { name: 'Humana', policy: 'HUM789123456' },
		submitted: '2024-04-12',
		amount: 240.0,
		status: 'Rejected',
		type: 'Medical',
	},
	{
		id: 'CLM-007',
		patient: { name: 'David Miller', id: '567890' },
		provider: { name: 'MetLife', policy: 'MET123456789' },
		submitted: 'Not submitted',
		amount: 180.0,
		status: 'Draft',
		type: 'Medical',
	},
])

// Computed properties
const filteredClaims = computed(() => {
	let filtered = claims.value

	// Filter by tab
	if (activeTab.value !== 'all') {
		filtered = filtered.filter((claim) => {
			if (activeTab.value === 'approved') return claim.status === 'Approved'
			if (activeTab.value === 'pending')
				return claim.status === 'Pending' || claim.status === 'Submitted'
			if (activeTab.value === 'rejected') return claim.status === 'Rejected'
			if (activeTab.value === 'draft') return claim.status === 'Draft'
			return true
		})
	}

	// Filter by search query
	if (searchQuery.value) {
		const query = searchQuery.value.toLowerCase()
		filtered = filtered.filter(
			(claim) =>
				claim.patient.name.toLowerCase().includes(query) ||
				claim.id.toLowerCase().includes(query) ||
				claim.provider.name.toLowerCase().includes(query),
		)
	}

	// Sort
	filtered.sort((a, b) => {
		switch (sortOrder.value) {
			case 'newest':
				if (a.submitted === 'Not submitted' && b.submitted === 'Not submitted') return 0
				if (a.submitted === 'Not submitted') return 1
				if (b.submitted === 'Not submitted') return -1
				return new Date(b.submitted) - new Date(a.submitted)
			case 'oldest':
				if (a.submitted === 'Not submitted' && b.submitted === 'Not submitted') return 0
				if (a.submitted === 'Not submitted') return 1
				if (b.submitted === 'Not submitted') return -1
				return new Date(a.submitted) - new Date(b.submitted)
			case 'amount-high':
				return b.amount - a.amount
			case 'amount-low':
				return a.amount - b.amount
			default:
				return 0
		}
	})

	return filtered
})

const stats = computed(() => {
	const total = claims.value.reduce((sum, claim) => sum + claim.amount, 0)
	const approved = claims.value
		.filter((c) => c.status === 'Approved')
		.reduce((sum, claim) => sum + claim.amount, 0)
	const pending = claims.value
		.filter((c) => c.status === 'Pending' || c.status === 'Submitted')
		.reduce((sum, claim) => sum + claim.amount, 0)

	return {
		total,
		approved,
		pending,
		totalCount: claims.value.length,
		approvedCount: claims.value.filter((c) => c.status === 'Approved').length,
		pendingCount: claims.value.filter(
			(c) => c.status === 'Pending' || c.status === 'Submitted',
		).length,
	}
})

const successRate = computed(() => {
	const submittedClaims = claims.value.filter((c) => c.submitted !== 'Not submitted')
	if (submittedClaims.length === 0) return 0
	const approvedClaims = submittedClaims.filter((c) => c.status === 'Approved')
	return Math.round((approvedClaims.length / submittedClaims.length) * 100)
})

// Methods
const getInitials = (name) => {
	return name
		.split(' ')
		.map((n) => n[0])
		.join('')
		.toUpperCase()
}

const getStatusClass = (status) => {
	switch (status) {
		case 'Approved':
			return 'bg-green-100 text-green-800'
		case 'Pending':
			return 'bg-yellow-100 text-yellow-800'
		case 'Submitted':
			return 'bg-blue-100 text-blue-800'
		case 'Rejected':
			return 'bg-red-100 text-red-800'
		case 'Draft':
			return 'bg-gray-100 text-gray-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

const getTypeClass = (type) => {
	switch (type) {
		case 'Medical':
			return 'bg-blue-50 text-blue-700 border border-blue-200'
		case 'Dental':
			return 'bg-purple-50 text-purple-700 border border-purple-200'
		default:
			return 'bg-gray-50 text-gray-700 border border-gray-200'
	}
}
</script>

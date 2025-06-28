<template>
	<div class="min-h-screen">
		<!-- Header -->
		<div class="bg-white px-4 sm:px-6 lg:px-8 py-6">
			<div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
				<div>
					<h1 class="text-2xl font-bold text-gray-900">Staff Management</h1>
					<p class="text-sm text-gray-600 mt-1">
						Manage clinic staff, roles, and permissions
					</p>
				</div>
				<div class="flex items-center gap-3">
					<button
						class="bg-gray-900 text-white px-4 py-2 rounded-sm text-sm font-medium hover:bg-gray-800 transition-colors flex items-center gap-2"
					>
						<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 6v6m0 0v6m0-6h6m-6 0H6"
							/>
						</svg>
						Add New Staff
					</button>
					<div class="relative">
						<button
							@click="showMoreOptions = !showMoreOptions"
							class="bg-white border border-gray-300 px-4 py-2 rounded-sm text-sm font-medium hover:bg-gray-50 transition-colors flex items-center gap-2"
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
									d="M9 12h6m-6 0a9 9 0 110 18 9 9 0 010-18zm6 0a9 9 0 110 18 9 9 0 010-18z"
								/>
							</svg>
							More Options
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
									d="M19 9l-7 7-7-7"
								/>
							</svg>
						</button>
					</div>
				</div>
			</div>
		</div>

		<div class="px-4 sm:px-6 lg:px-8 py-6">
			<div class="flex flex-col xl:flex-row gap-6">
				<!-- Main Content -->
				<div class="flex-1">
					<!-- Staff Directory Header -->
					<div class="bg-white rounded-sm shadow-sm border border-gray-200">
						<div class="px-6 py-4 border-b border-gray-200">
							<div
								class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4"
							>
								<h2 class="text-lg font-semibold text-gray-900">
									Staff Directory
								</h2>
								<div class="flex items-center gap-4">
									<!-- Search -->
									<div class="relative flex-1 sm:flex-none sm:w-64">
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
											placeholder="Search staff..."
											class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent w-full"
										/>
									</div>
									<!-- Filter -->
									<button
										class="p-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
									>
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
												d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
											/>
										</svg>
									</button>
								</div>
							</div>
							<!-- View Toggle -->
							<div class="flex items-center gap-2 mt-4">
								<button
									@click="viewMode = 'list'"
									:class="[
										'px-3 py-1 text-sm rounded-md font-medium transition-colors',
										viewMode === 'list'
											? 'bg-blue-100 text-blue-700'
											: 'text-gray-600 hover:text-gray-900',
									]"
								>
									List View
								</button>
								<button
									@click="viewMode = 'grid'"
									:class="[
										'px-3 py-1 text-sm rounded-md font-medium transition-colors',
										viewMode === 'grid'
											? 'bg-blue-100 text-blue-700'
											: 'text-gray-600 hover:text-gray-900',
									]"
								>
									Grid View
								</button>
							</div>
						</div>

						<!-- Staff List -->
						<div class="overflow-x-auto">
							<table class="w-full" v-if="viewMode === 'list'">
								<thead class="bg-gray-50 border-b border-gray-200">
									<tr>
										<th
											class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
										>
											Name
										</th>
										<th
											class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden sm:table-cell"
										>
											Role
										</th>
										<th
											class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden md:table-cell"
										>
											Department
										</th>
										<th
											class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden lg:table-cell"
										>
											Contact
										</th>
										<th
											class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider hidden lg:table-cell"
										>
											Joined
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
										v-for="staff in filteredStaff"
										:key="staff.id"
										class="hover:bg-gray-50 transition-colors"
									>
										<td class="px-6 py-4 whitespace-nowrap">
											<div class="flex items-center">
												<div
													class="h-10 w-10 rounded-full bg-gray-300 flex items-center justify-center text-white font-medium text-sm"
												>
													{{
														staff.name
															.split(' ')
															.map((n) => n[0])
															.join('')
													}}
												</div>
												<div class="ml-3">
													<div class="text-sm font-medium text-gray-900">
														{{ staff.name }}
													</div>
													<div class="text-sm text-gray-500 sm:hidden">
														{{ staff.role }}
													</div>
												</div>
											</div>
										</td>
										<td
											class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 hidden sm:table-cell"
										>
											{{ staff.role }}
										</td>
										<td
											class="px-6 py-4 whitespace-nowrap hidden md:table-cell"
										>
											<span
												:class="[
													'inline-flex px-2 py-1 text-xs font-medium rounded-full',
													getDepartmentColor(staff.department),
												]"
											>
												{{ staff.department }}
											</span>
										</td>
										<td
											class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden lg:table-cell"
										>
											<div>{{ staff.email }}</div>
											<div>{{ staff.phone }}</div>
										</td>
										<td
											class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 hidden lg:table-cell"
										>
											{{ staff.joined }}
										</td>
										<td class="px-6 py-4 whitespace-nowrap">
											<span
												:class="[
													'inline-flex px-2 py-1 text-xs font-medium rounded-full',
													getStatusColor(staff.status),
												]"
											>
												{{ staff.status }}
											</span>
										</td>
										<td
											class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
										>
											<button
												class="text-gray-400 hover:text-gray-600 transition-colors"
											>
												<svg
													class="w-5 h-5"
													fill="currentColor"
													viewBox="0 0 20 20"
												>
													<path
														d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"
													/>
												</svg>
											</button>
										</td>
									</tr>
								</tbody>
							</table>

							<!-- Grid View -->
							<div
								v-else
								class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 p-6"
							>
								<div
									v-for="staff in filteredStaff"
									:key="staff.id"
									class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
								>
									<div class="flex items-center justify-between mb-3">
										<div
											class="h-12 w-12 rounded-full bg-gray-300 flex items-center justify-center text-white font-medium"
										>
											{{
												staff.name
													.split(' ')
													.map((n) => n[0])
													.join('')
											}}
										</div>
										<span
											:class="[
												'inline-flex px-2 py-1 text-xs font-medium rounded-full',
												getStatusColor(staff.status),
											]"
										>
											{{ staff.status }}
										</span>
									</div>
									<h3 class="font-medium text-gray-900 mb-1">
										{{ staff.name }}
									</h3>
									<p class="text-sm text-gray-600 mb-2">{{ staff.role }}</p>
									<span
										:class="[
											'inline-flex px-2 py-1 text-xs font-medium rounded-full mb-2',
											getDepartmentColor(staff.department),
										]"
									>
										{{ staff.department }}
									</span>
									<div class="text-xs text-gray-500">
										<div>{{ staff.email }}</div>
										<div>Joined {{ staff.joined }}</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>

				<!-- Sidebar -->
				<div class="xl:w-80 space-y-6">
					<!-- Staff Overview -->
					<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
						<div class="flex items-center justify-between mb-4">
							<h3 class="text-lg font-semibold text-gray-900">Staff Overview</h3>
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
									d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
								/>
							</svg>
						</div>
						<div class="text-3xl font-bold text-gray-900 mb-1">{{ totalStaff }}</div>
						<p class="text-sm text-gray-600 mb-4">Total Staff</p>

						<div class="space-y-3">
							<div class="flex items-center justify-between">
								<span class="text-sm text-gray-600">Active</span>
								<div class="flex items-center gap-2">
									<span class="text-sm font-medium text-gray-900">{{
										activeStaff
									}}</span>
									<span class="text-xs text-gray-500"
										>{{ Math.round((activeStaff / totalStaff) * 100) }}%</span
									>
								</div>
							</div>
							<div class="flex items-center justify-between">
								<span class="text-sm text-gray-600">On Leave</span>
								<div class="flex items-center gap-2">
									<span class="text-sm font-medium text-gray-900">{{
										onLeaveStaff
									}}</span>
									<span class="text-xs text-gray-500"
										>{{ Math.round((onLeaveStaff / totalStaff) * 100) }}%</span
									>
								</div>
							</div>
							<div class="flex items-center justify-between">
								<span class="text-sm text-gray-600">Inactive</span>
								<div class="flex items-center gap-2">
									<span class="text-sm font-medium text-gray-900">{{
										inactiveStaff
									}}</span>
									<span class="text-xs text-gray-500"
										>{{
											Math.round((inactiveStaff / totalStaff) * 100)
										}}%</span
									>
								</div>
							</div>
						</div>
					</div>

					<!-- Departments -->
					<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Departments</h3>
						<div class="space-y-3">
							<div
								v-for="dept in departments"
								:key="dept.name"
								class="flex items-center justify-between"
							>
								<div class="flex items-center gap-2">
									<div :class="['w-3 h-3 rounded-full', dept.color]"></div>
									<span class="text-sm text-gray-900">{{ dept.name }}</span>
								</div>
								<span class="text-sm font-medium text-gray-600">{{
									dept.count
								}}</span>
							</div>
						</div>
						<button
							class="mt-4 w-full text-left text-sm text-blue-600 hover:text-blue-700 transition-colors flex items-center gap-2"
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
									d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								/>
							</svg>
							Manage Departments
						</button>
					</div>
					<!-- Departments -->
					<div class="bg-white rounded-sm shadow-sm border border-gray-200 p-6">
						<h3 class="text-lg font-semibold text-gray-900 mb-4">Departments</h3>
						<div class="space-y-3">
							<div
								v-for="dept in departments"
								:key="dept.name"
								class="flex items-center justify-between"
							>
								<div class="flex items-center gap-2">
									<div :class="['w-3 h-3 rounded-full', dept.color]"></div>
									<span class="text-sm text-gray-900">{{ dept.name }}</span>
								</div>
								<span class="text-sm font-medium text-gray-600">{{
									dept.count
								}}</span>
							</div>
						</div>
						<button
							class="mt-4 w-full text-left text-sm text-blue-600 hover:text-blue-700 transition-colors flex items-center gap-2"
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
									d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
								/>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
								/>
							</svg>
							Manage Departments
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Reactive data
const searchQuery = ref('')
const viewMode = ref('list')
const showMoreOptions = ref(false)

// Sample staff data
const staffData = ref([
	{
		id: 1,
		name: 'Dr. Sarah Johnson',
		role: 'Cardiologist',
		department: 'Medical',
		email: 'sarah.j@clinic.com',
		phone: '555-0101',
		joined: 'May 15, 2012',
		status: 'Active',
	},
	{
		id: 2,
		name: 'Dr. Michael Chen',
		role: 'Neurologist',
		department: 'Medical',
		email: 'michael.c@clinic.com',
		phone: '555-0102',
		joined: 'Jun 22, 2015',
		status: 'Active',
	},
	{
		id: 3,
		name: 'Emma Rodriguez',
		role: 'Head Nurse',
		department: 'Nursing',
		email: 'emma.r@clinic.com',
		phone: '555-0103',
		joined: 'Feb 10, 2018',
		status: 'On Leave',
	},
	{
		id: 4,
		name: 'Robert Davis',
		role: 'Lab Technician',
		department: 'Laboratory',
		email: 'robert.d@clinic.com',
		phone: '555-0104',
		joined: 'Nov 5, 2019',
		status: 'Active',
	},
	{
		id: 5,
		name: 'Jennifer Kim',
		role: 'Pharmacist',
		department: 'Pharmacy',
		email: 'jennifer.k@clinic.com',
		phone: '555-0105',
		joined: 'Mar 18, 2017',
		status: 'Active',
	},
	{
		id: 6,
		name: 'David Wilson',
		role: 'Radiologist',
		department: 'Radiology',
		email: 'david.w@clinic.com',
		phone: '555-0106',
		joined: 'Sep 30, 2016',
		status: 'Inactive',
	},
	{
		id: 7,
		name: 'Maria Garcia',
		role: 'Receptionist',
		department: 'Administration',
		email: 'maria.g@clinic.com',
		phone: '555-0107',
		joined: 'Jan 12, 2020',
		status: 'Active',
	},
	{
		id: 8,
		name: 'James Brown',
		role: 'Physical Therapist',
		department: 'Therapy',
		email: 'james.b@clinic.com',
		phone: '555-0108',
		joined: 'Jul 7, 2018',
		status: 'Active',
	},
	{
		id: 9,
		name: 'James Brown',
		role: 'Physical Therapist',
		department: 'Therapy',
		email: 'james.b@clinic.com',
		phone: '555-0108',
		joined: 'Jul 7, 2018',
		status: 'Active',
	},
	{
		id: 10,
		name: 'James Brown',
		role: 'Physical Therapist',
		department: 'Therapy',
		email: 'james.b@clinic.com',
		phone: '555-0108',
		joined: 'Jul 7, 2018',
		status: 'Active',
	},
])

// Computed properties
const filteredStaff = computed(() => {
	if (!searchQuery.value) return staffData.value

	return staffData.value.filter(
		(staff) =>
			staff.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			staff.role.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
			staff.department.toLowerCase().includes(searchQuery.value.toLowerCase()),
	)
})

const totalStaff = computed(() => staffData.value.length)
const activeStaff = computed(() => staffData.value.filter((s) => s.status === 'Active').length)
const onLeaveStaff = computed(() => staffData.value.filter((s) => s.status === 'On Leave').length)
const inactiveStaff = computed(() => staffData.value.filter((s) => s.status === 'Inactive').length)

const departments = computed(() => {
	const deptCounts = staffData.value.reduce((acc, staff) => {
		acc[staff.department] = (acc[staff.department] || 0) + 1
		return acc
	}, {})

	const deptColors = {
		Medical: 'bg-blue-500',
		Nursing: 'bg-green-500',
		Administration: 'bg-purple-500',
		Laboratory: 'bg-orange-500',
		Pharmacy: 'bg-red-500',
		Radiology: 'bg-indigo-500',
		Therapy: 'bg-pink-500',
		Support: 'bg-cyan-500',
	}

	return Object.entries(deptCounts).map(([name, count]) => ({
		name,
		count,
		color: deptColors[name] || 'bg-gray-500',
	}))
})

// Methods
const getStatusColor = (status) => {
	switch (status) {
		case 'Active':
			return 'bg-green-100 text-green-800'
		case 'On Leave':
			return 'bg-yellow-100 text-yellow-800'
		case 'Inactive':
			return 'bg-gray-100 text-gray-800'
		default:
			return 'bg-gray-100 text-gray-800'
	}
}

const getDepartmentColor = (department) => {
	const colors = {
		Medical: 'bg-blue-100 text-blue-800',
		Nursing: 'bg-green-100 text-green-800',
		Administration: 'bg-purple-100 text-purple-800',
		Laboratory: 'bg-orange-100 text-orange-800',
		Pharmacy: 'bg-red-100 text-red-800',
		Radiology: 'bg-indigo-100 text-indigo-800',
		Therapy: 'bg-pink-100 text-pink-800',
		Support: 'bg-cyan-100 text-cyan-800',
	}
	return colors[department] || 'bg-gray-100 text-gray-800'
}
</script>
